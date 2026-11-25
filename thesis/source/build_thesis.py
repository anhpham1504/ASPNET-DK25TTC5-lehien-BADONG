"""Build the editable thesis and bibliography from the tracked Markdown and JSON."""

import json
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image


SOURCE = Path(__file__).resolve().parent
THESIS = SOURCE.parent
REPOSITORY = THESIS.parent
FONT = "Times New Roman"
CONTENT_WIDTH = 16
ACCESS_DATE = "2026-11-25"
CITATION = re.compile(r"\[@([a-z0-9-]+)\]")
MARKUP = re.compile(r"\[@([a-z0-9-]+)\]|\[([^\]]+)\]\((https?://[^\s)]+)\)|`([^`]+)`")


def element(tag, **attributes):
    node = OxmlElement(f"w:{tag}")
    for key, value in attributes.items():
        node.set(qn(f"w:{key}"), str(value))
    return node


def set_fonts(properties):
    fonts = properties.rFonts
    if fonts is None:
        fonts = element("rFonts")
        properties.insert(0, fonts)
    for key in list(fonts.attrib):
        del fonts.attrib[key]
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{key}"), FONT)


def field(paragraph, instruction, cached=""):
    paragraph.add_run()._r.append(element("fldChar", fldCharType="begin"))
    run = paragraph.add_run()
    code = element("instrText")
    code.set(qn("xml:space"), "preserve")
    code.text = f" {instruction} "
    run._r.append(code)
    paragraph.add_run()._r.append(element("fldChar", fldCharType="separate"))
    if cached:
        paragraph.add_run(cached)
    paragraph.add_run()._r.append(element("fldChar", fldCharType="end"))


def link(paragraph, label, url):
    rel = paragraph.part.relate_to(url, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    node = element("hyperlink")
    node.set(qn("r:id"), rel)
    run = element("r")
    props = element("rPr")
    props.append(element("u", val="single"))
    run.append(props)
    txt = element("t")
    txt.text = label
    run.append(txt)
    node.append(run)
    paragraph._p.append(node)


def configure_styles(doc):
    for style in doc.styles:
        if style.type.name not in ("PARAGRAPH", "CHARACTER"):
            continue
        style.font.name = FONT
        style.font.size = Pt(13)
        style.font.color.rgb = RGBColor(0, 0, 0)
        set_fonts(style.element.get_or_add_rPr())
        lang = style.element.rPr.find(qn("w:lang"))
        if lang is None:
            lang = element("lang", val="vi-VN")
            style.element.rPr.append(lang)
        else:
            lang.set(qn("w:val"), "vi-VN")
    normal = doc.styles["Normal"]
    normal.paragraph_format.space_before = Pt(6)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal.paragraph_format.first_line_indent = Cm(0.7)
    normal.paragraph_format.widow_control = True
    for name in ("Title", "Subtitle", "Heading 1", "Heading 2", "Heading 3", "Caption", "Footer"):
        style = doc.styles[name]
        style.paragraph_format.first_line_indent = Cm(0)
        style.paragraph_format.space_before = Pt(6)
        style.paragraph_format.space_after = Pt(6)
        style.paragraph_format.line_spacing = 1.5
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        style.font.italic = False
        props = style.element.get_or_add_pPr()
        border = props.find(qn("w:pBdr"))
        if border is not None:
            props.remove(border)
    for name in ("Title", "Heading 1", "Heading 2", "Heading 3"):
        style = doc.styles[name]
        style.font.bold = True
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.keep_together = True
    doc.styles["Title"].font.size = Pt(22)
    doc.styles["Caption"].font.italic = True
    for name in ("Front Heading", "Entry", "Table Cell", "Sample", "Illustration"):
        style = doc.styles.add_style(name, normal.type)
        style.base_style = normal
        style.paragraph_format.first_line_indent = Cm(0)
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    doc.styles["Front Heading"].font.bold = True
    doc.styles["Front Heading"].paragraph_format.keep_with_next = True
    doc.styles["Illustration"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.styles["Illustration"].paragraph_format.keep_with_next = True
    doc.styles["Sample"].paragraph_format.left_indent = Cm(0.5)
    doc.styles["Sample"].paragraph_format.keep_together = True
    doc.styles["Entry"].paragraph_format.left_indent = Cm(0.85)
    doc.styles["Entry"].paragraph_format.first_line_indent = Cm(-0.85)
    doc.styles["Entry"].paragraph_format.keep_together = True
    for name, indent in (("TOC 1", 0), ("TOC 2", 0.45), ("TOC 3", 0.9), ("Table of Figures", 0)):
        if name not in doc.styles:
            doc.styles.add_style(name, normal.type)
        style = doc.styles[name]
        style.base_style = normal
        style.paragraph_format.first_line_indent = Cm(0)
        style.paragraph_format.left_indent = Cm(indent)
        style.paragraph_format.space_before = Pt(0)
        style.paragraph_format.space_after = Pt(0)
        style.paragraph_format.line_spacing = 1.15
        style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        style.paragraph_format.tab_stops.add_tab_stop(Cm(CONTENT_WIDTH), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)


def configure_page(section):
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.left_margin, section.right_margin = Cm(3), Cm(2)
    section.top_margin, section.bottom_margin = Cm(2), Cm(2)
    section.footer_distance = Cm(0.85)


def bibliography():
    items = json.loads((SOURCE / "references.json").read_text(encoding="utf-8"))
    identifiers = {item["id"]: idx for idx, item in enumerate(items, 1)}
    if len(items) != len(identifiers):
        raise ValueError("Duplicate bibliography key")
    return items, identifiers


class ThesisBuilder:
    def __init__(self):
        self.doc = Document()
        self.items, self.ids = bibliography()
        self.used = set()
        self.figures = 0
        self.tables = 0
        configure_styles(self.doc)
        configure_page(self.doc.sections[0])
        self.doc.core_properties.author = "Lê Hiền"
        self.doc.core_properties.title = "BA ĐỘNG — Coastal Escape"
        self.doc.core_properties.subject = "Đồ án Chuyên đề ASP.NET"
        self.doc.core_properties.language = "vi-VN"
        self.doc.core_properties.comments = ""

    def rich(self, p, text):
        position = 0
        for hit in MARKUP.finditer(text):
            p.add_run(text[position:hit.start()])
            key, label, url, literal = hit.groups()
            if key:
                self.used.add(key)
                p.add_run(f"[{self.ids[key]}]")
            elif url:
                link(p, label, url)
            else:
                p.add_run(literal)
            position = hit.end()
        if position < len(text):
            p.add_run(text[position:])
        return p

    def paragraph(self, text, style=None):
        return self.rich(self.doc.add_paragraph(style=style), text)

    def front_heading(self, title, new_page=True):
        p = self.paragraph(title, "Front Heading")
        p.paragraph_format.page_break_before = new_page
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return p

    def cover(self, kind, new_page):
        p = self.front_heading("[TÊN TRƯỜNG]", new_page)
        p.paragraph_format.space_before = Pt(24)
        for label in ("[TÊN KHOA]", kind, "ĐỒ ÁN MÔN HỌC CHUYÊN ĐỀ ASP.NET"):
            p = self.paragraph(label, "Front Heading")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(95)
        p = self.paragraph("BA ĐỘNG — Coastal Escape", "Title")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for label in ("Sinh viên thực hiện  Lê Hiền", "Mã số sinh viên  170125405", "Lớp  DK25TTC5",
                      "Giảng viên hướng dẫn  [HỌ VÀ TÊN GVHD]", "Email  [EMAIL SINH VIÊN]", "Điện thoại  [SỐ ĐIỆN THOẠI SINH VIÊN]"):
            self.paragraph(label, "Table Cell")
        p = self.paragraph("[ĐỊA DANH] · 2026\nKhung trình bày chờ mẫu được xác nhận.")
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(65)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def review(self, group):
        self.front_heading(f"NHẬN XÉT CỦA {group}")
        self.paragraph("Đề tài  BA ĐỘNG — Coastal Escape", "Table Cell")
        self.paragraph("Sinh viên  Lê Hiền     MSSV  170125405     Lớp  DK25TTC5", "Table Cell")
        self.paragraph("[MẪU NHẬN XÉT CHỜ XÁC NHẬN]", "Table Cell")
        self.paragraph("[NỘI DUNG DÀNH CHO NGƯỜI NHẬN XÉT]", "Table Cell")

    def start_numbered(self):
        section = self.doc.add_section(WD_SECTION.NEW_PAGE)
        configure_page(section)
        section.footer.is_linked_to_previous = False
        section._sectPr.append(element("pgNumType", start=1, fmt="decimal"))
        p = section.footer.paragraphs[0]
        p.style = "Footer"
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        field(p, "PAGE", "1")

    def caption(self, label, index, title, keep_next):
        p = self.doc.add_paragraph(style="Caption")
        p.paragraph_format.keep_with_next = keep_next
        p.paragraph_format.keep_together = True
        p.add_run(label + " ")
        field(p, f'SEQ {"Fig" if label == "Hình" else "Tbl"} \\* ARABIC', str(index))
        self.rich(p, ". " + title)

    def table(self, title, widths, rows):
        self.tables += 1
        self.caption("Bảng", self.tables, title, True)
        table = self.doc.add_table(rows=0, cols=len(widths))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        for column, fraction in zip(table.columns, widths):
            column.width = Cm(CONTENT_WIDTH * fraction)
        props = table._tbl.tblPr
        borders = element("tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            borders.append(element(edge, val="single", sz=5, color="D9D9D9"))
        props.append(borders)
        padding = element("tblCellMar")
        for side in ("left", "right", "top", "bottom"):
            padding.append(element(side, w=85, type="dxa"))
        props.append(padding)
        for idx, values in enumerate(rows):
            if len(values) != len(widths):
                raise ValueError(f"Wrong column count in table: {title}")
            row = table.add_row()
            row._tr.get_or_add_trPr().append(element("cantSplit"))
            if idx == 0:
                row._tr.trPr.append(element("tblHeader"))
            for cell, value, fraction in zip(row.cells, values, widths):
                cell.width = Cm(CONTENT_WIDTH * fraction)
                cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                p = cell.paragraphs[0]
                p.style = "Table Cell"
                p.paragraph_format.space_before = Pt(3)
                p.paragraph_format.space_after = Pt(3)
                self.rich(p, value)
                if idx == 0:
                    p.paragraph_format.keep_with_next = True
                    cell._tc.get_or_add_tcPr().append(element("shd", fill="ECECEC"))
                    for run in p.runs:
                        run.bold = True

    def figure(self, names, title, max_height=17):
        self.figures += 1
        paths = [REPOSITORY / name for name in names.split(";")]
        p = self.doc.add_paragraph(style="Illustration")
        for idx, path in enumerate(paths):
            if idx:
                p.add_run("   ")
            with Image.open(path) as image:
                width, height = image.size
            cap_w = CONTENT_WIDTH if len(paths) == 1 else (CONTENT_WIDTH - 0.65 * (len(paths) - 1)) / len(paths)
            cm = min(cap_w, (max_height if len(paths) == 1 else 10) * width / height)
            pic = p.add_run().add_picture(str(path), width=Cm(cm))
            pic._inline.docPr.set("descr", f"{title} · {path.stem}")
        self.caption("Hình", self.figures, title, False)

    def write_bibliography(self):
        for item in self.items:
            date = f", {item['year']}" if item.get("year") else ""
            p = self.paragraph(f"[{self.ids[item['id']]}] {item['author']}, “{item['title']}”{date}. [Trực tuyến]. ", "Entry")
            p.add_run("Truy cập 25/11/2026.").add_break()
            display_url = re.sub(r"([/?=&_%.-])", lambda match: match[0] + "\u200b", item["url"])
            link(p, display_url, item["url"])

    def render_blocks(self, path, front=False):
        blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8").strip())
        for block in blocks:
            lines = block.splitlines()
            main = lines[0]
            if main.startswith("!table|"):
                _, title, fractions = main.split("|", 2)
                rows = [[cell.strip() for cell in row.strip().strip("|").split("|")] for row in lines[1:]]
                self.table(title, [float(item) for item in fractions.split(",")], rows)
            elif main.startswith("!figure|"):
                _, names, title, *limit = main.split("|")
                self.figure(names, title, float(limit[0]) if limit else 17)
            elif main.startswith("#"):
                heading, title = main.split(" ", 1)
                level = len(heading)
                if front:
                    self.front_heading(title, new_page=title != "LỜI CẢM ƠN")
                else:
                    p = self.paragraph(title, f"Heading {level}")
                    if level == 1:
                        p.paragraph_format.page_break_before = True
            elif main == "!toc":
                field(self.doc.add_paragraph(style="Table Cell"), 'TOC \\o "1-3" \\h \\z \\u')
            elif main in ("!lof", "!lot"):
                seq = "Fig" if main == "!lof" else "Tbl"
                field(self.doc.add_paragraph(style="Table Cell"), f'TOC \\h \\z \\c "{seq}"')
            elif main == "!refs":
                self.write_bibliography()
            elif main.startswith("> "):
                self.paragraph("\n".join(line.removeprefix("> ") for line in lines), "Sample")
            else:
                self.paragraph(" ".join(lines))

    def build(self):
        self.cover("BÌA CHÍNH", False)
        self.cover("BÌA PHỤ", True)
        self.review("GIẢNG VIÊN HƯỚNG DẪN")
        self.review("THÀNH VIÊN HỘI ĐỒNG")
        self.start_numbered()
        self.render_blocks(SOURCE / "00-front.md", front=True)
        for file in sorted(SOURCE.glob("[1-8][0-9]-*.md")):
            self.render_blocks(file)
        expected = set(self.ids)
        if self.used != expected:
            raise ValueError(f"Uncited sources: {expected - self.used}")
        destination = THESIS / "doc" / "BA-DONG-Coastal-Escape.docx"
        self.doc.save(destination)
        write_refs(self.items)
        print(f"{destination.name}: {self.figures} figures, {self.tables} tables, {len(self.items)} references")


def write_refs(items):
    text = [
        "# Tài liệu đã trích dẫn",
        "",
        "Các mục theo trật tự từ điển của tác giả hoặc tổ chức, rồi theo tiêu đề khi cùng tác giả. "
        "Mỗi mục dùng hình thức tham chiếu IEEE. Cách kết hợp hai yêu cầu của PDF cần được giảng viên xác nhận.",
        "",
    ]
    bib = []
    for idx, item in enumerate(items, 1):
        year = f", {item['year']}" if item.get("year") else ""
        text.extend([
            f"[{idx}] {item['author']}, “{item['title']}”{year}. Trực tuyến. Truy cập 25/11/2026.",
            f"    <{item['url']}>",
            f"    Sử dụng cho {item['use']}.",
            "",
        ])
        fields = {
            "author": "{" + item["author"] + "}",
            "title": item["title"],
            **({"year": item["year"]} if item.get("year") else {}),
            "howpublished": item["url"],
            "note": f"Accessed {ACCESS_DATE}. IEEE identifier [{idx}]",
        }
        bib.append(f"@misc{{{item['id']},\n" + ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items()) + "\n}")
    (THESIS / "refs" / "REFERENCES.md").write_text("\n".join(text), encoding="utf-8")
    (THESIS / "refs" / "references.bib").write_text("\n\n".join(bib) + "\n", encoding="utf-8")


if __name__ == "__main__":
    ThesisBuilder().build()
