"""Validate the exported DOCX/PDF pair and print observed pagination and counts."""

import json
import re
from pathlib import Path

import pdfplumber
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent.parent
NAME = "BA-DONG-Coastal-Escape"
HEADINGS = (
    "MỞ ĐẦU",
    "CHƯƠNG 1. TỔNG QUAN",
    "CHƯƠNG 2. NGHIÊN CỨU LÝ THUYẾT",
    "CHƯƠNG 3. HIỆN THỰC HÓA NGHIÊN CỨU",
    "CHƯƠNG 4. KẾT QUẢ NGHIÊN CỨU",
    "CHƯƠNG 5. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN",
    "DANH MỤC TÀI LIỆU THAM KHẢO",
    "PHỤ LỤC",
)


def main():
    doc = Document(ROOT / "doc" / f"{NAME}.docx")
    pdf_path = ROOT / "pdf" / f"{NAME}.pdf"
    pdf = PdfReader(pdf_path)
    references = json.loads((ROOT / "source" / "references.json").read_text(encoding="utf-8"))
    for section in doc.sections:
        sizes = [getattr(section, item).cm for item in (
            "page_width", "page_height", "top_margin", "bottom_margin", "left_margin", "right_margin",
        )]
        assert all(abs(actual - target) < 0.03 for actual, target in zip(sizes, (21, 29.7, 2, 2, 3, 2))), sizes
    normal = doc.styles["Normal"]
    assert normal.font.name == "Times New Roman" and normal.font.size.pt == 13
    assert normal.paragraph_format.line_spacing == 1.5
    assert normal.paragraph_format.space_before.pt == normal.paragraph_format.space_after.pt == 6
    assert all(pic._inline.docPr.get("descr") for pic in doc.inline_shapes)

    page_text = [page.extract_text() for page in pdf.pages]
    assert all(text.strip() for text in page_text)
    for page in pdf.pages:
        assert abs(float(page.mediabox.width) - 595.28) < 1
        assert abs(float(page.mediabox.height) - 841.89) < 1
    assert not re.search(r"Error! (?:Reference|No)|\uFFFD|\[@[a-z0-9-]+\]", "\n".join(page_text))
    page_lines = [[line.strip() for line in text.splitlines() if line.strip()] for text in page_text]
    assert all(lines[0] == str(index - 4) for index, lines in enumerate(page_lines[4:], 5))
    starts = {
        heading: next(index for index, lines in enumerate(page_lines, 1) if heading in lines[:3])
        for heading in HEADINGS
    }
    sections = {
        a: starts[b] - starts[a]
        for a, b in zip(HEADINGS[:6], HEADINGS[1:7])
    }
    total_main = sum(sections.values())
    assert 30 <= total_main <= 50, total_main
    front = "\n".join(page_text[:starts[HEADINGS[0]] - 1])
    for heading in HEADINGS:
        assert re.search(re.escape(heading) + r"\s*\.+\s+" + str(starts[heading] - 4) + r"\b", front), heading
    instructions = [str(n.text).strip() for n in doc.element.iter(qn("w:instrText"))]
    assert any(code.startswith("TOC") and '"1-3"' in code for code in instructions)
    assert all(any(code.startswith("TOC") and f'"{seq}"' in code for code in instructions) for seq in ("Fig", "Tbl"))
    figures = sum(code.startswith("SEQ Fig") for code in instructions)
    tables = sum(code.startswith("SEQ Tbl") for code in instructions)
    assert len(doc.tables) == tables
    for word, count in (("Hình", figures), ("Bảng", tables)):
        # pypdf may insert a space before the caption-number period when Word
        # justifies a wrapped entry in the list of figures or tables.
        assert set(re.findall(r"(?m)^" + word + r" (\d+)\s*\.", front)) == set(map(str, range(1, count + 1)))
    refs_text = "\n".join(page_text[starts[HEADINGS[6]] - 1:starts[HEADINGS[7]] - 1])
    refs_numbers = list(map(int, re.findall(r"(?m)^\s*\[(\d+)\]", refs_text)))
    assert refs_numbers == list(range(1, len(references) + 1))

    for index, page in enumerate(pdfplumber.open(pdf_path).pages, 1):
        body_chars = [c for c in page.chars if c["text"].strip()]
        assert all("TimesNewRoman" in c["fontname"] for c in body_chars), index
        assert all(84 <= c["x0"] and c["x1"] <= 540 for c in body_chars), index
        if index > 4:
            footer = [c for c in body_chars if c["top"] > 790]
            assert footer and all(c["x0"] > 500 for c in footer), index

    print(json.dumps({
        "physical_pages": len(pdf.pages),
        "chapter_start_pdf_pages": starts,
        "main_pages": total_main,
        "chapter_pages": sections,
        "figures": figures,
        "embedded_images": len(doc.inline_shapes),
        "tables": tables,
        "references": len(references),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
