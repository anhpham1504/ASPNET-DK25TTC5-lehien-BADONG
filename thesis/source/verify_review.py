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
    for index, lines in enumerate(page_lines, 1):
        content = lines[1:] if lines and lines[0].isdigit() else lines
        assert content, f"Footer-only or blank physical page: {index}"
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

    def normalized(value):
        return re.sub(r"\s+", " ", value).strip()

    def displayed_page_for_line(pattern, start_page):
        for page_index in range(start_page - 1, len(page_lines)):
            if any(re.match(pattern, line) for line in page_lines[page_index]):
                return int(page_lines[page_index][0])
        raise AssertionError(f"Content not found in PDF: {pattern}")

    # Verify every cached TOC page number against the final PDF, not only the
    # chapter starts. This catches a DOCX saved before Word's final pagination.
    heading_pages = []
    page_cursor = starts[HEADINGS[0]] - 1
    for paragraph in doc.paragraphs:
        if not paragraph.style.name.startswith("Heading "):
            continue
        title = normalized(paragraph.text)
        found = None
        for page_index in range(page_cursor, len(page_lines)):
            if any(normalized(line) == title for line in page_lines[page_index]):
                found = page_index
                break
        assert found is not None, f"Heading not found in PDF: {title}"
        heading_pages.append((title, int(page_lines[found][0])))
        page_cursor = found

    records = []
    for paragraph in doc.element.body.iterchildren():
        if paragraph.tag != qn("w:p"):
            continue
        properties = paragraph.find(qn("w:pPr"))
        style = properties.find(qn("w:pStyle")) if properties is not None else None
        style_id = style.get(qn("w:val")) if style is not None else ""
        parts = []
        for node in paragraph.iter():
            if node.tag == qn("w:t"):
                parts.append(node.text or "")
            elif node.tag == qn("w:tab"):
                parts.append("\t")
        records.append((style_id, "".join(parts).strip()))

    toc_records = [text for style, text in records if style in {"TOC1", "TOC2", "TOC3"}]
    toc_cursor = 0
    for title, actual_page in heading_pages:
        match = None
        for index in range(toc_cursor, len(toc_records)):
            if title in toc_records[index]:
                match = index
                break
        assert match is not None, f"TOC entry not found for heading: {title}"
        cached = re.search(r"\t(\d+)\s*$", toc_records[match])
        assert cached and int(cached.group(1)) == actual_page, (title, cached.group(1) if cached else None, actual_page)
        toc_cursor = match + 1

    figure_records = [text for style, text in records if style == "TableofFigures"]
    for label, count in (("Hình", figures), ("Bảng", tables)):
        indexed = {int(hit.group(1)): (text, int(hit.group(2))) for text in figure_records
                   if (hit := re.match(rf"{label} (\d+)\..*\t(\d+)\s*$", text))}
        assert set(indexed) == set(range(1, count + 1)), (label, sorted(indexed))
        for number in range(1, count + 1):
            actual_page = displayed_page_for_line(rf"^{label} {number}\.\s", starts[HEADINGS[0]])
            assert indexed[number][1] == actual_page, (label, number, indexed[number][1], actual_page)
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
        "toc_entries": len(toc_records),
        "figures": figures,
        "embedded_images": len(doc.inline_shapes),
        "tables": tables,
        "references": len(references),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
