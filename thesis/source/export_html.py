"""Export the offline thesis from the same marked-up chapters as Word."""

from html import escape
from pathlib import Path
import re

from build_thesis import MARKUP, REPOSITORY, SOURCE, THESIS, bibliography


def blocks(path):
    return re.split(r"\n\s*\n", path.read_text(encoding="utf-8").strip())


class HtmlThesis:
    def __init__(self):
        self.items, self.ids = bibliography()
        self.figures = []
        self.tables = []
        self.chapters = []
        self.used = set()

    def rich(self, source):
        output = []
        start = 0
        for match in MARKUP.finditer(source):
            output.append(escape(source[start:match.start()]))
            key, label, url, literal = match.groups()
            if key:
                self.used.add(key)
                output.append(f'<a class="citation" href="#ref-{key}">[{self.ids[key]}]</a>')
            elif url:
                output.append(f'<a href="{escape(url, quote=True)}">{escape(label)}</a>')
            else:
                output.append(f'<code>{escape(literal)}</code>')
            start = match.end()
        output.append(escape(source[start:]))
        return "".join(output)

    def heading(self, line, path, index, front):
        marker, title = line.split(" ", 1)
        level = len(marker) + 1
        anchor = f"{path.stem}-{index}"
        if not front and level == 2:
            self.chapters.append((anchor, title))
        return f'<h{level} id="{anchor}">{escape(title)}</h{level}>'

    def figure(self, line):
        _, paths, caption, *_ = line.split("|")
        index = len(self.figures) + 1
        self.figures.append((f"figure-{index}", f"Hình {index}. {caption}"))
        images = []
        for subindex, path in enumerate(paths.split(";"), 1):
            image = REPOSITORY / path
            if not image.is_file():
                raise FileNotFoundError(image)
            suffix = f", ảnh {subindex}" if ";" in paths else ""
            images.append(f'<img src="../../{escape(path, quote=True)}" alt="{escape(caption + suffix, quote=True)}" loading="lazy">')
        return (f'<figure id="figure-{index}"><div class="figure-images">{"".join(images)}</div>'
                f'<figcaption>{self.rich(self.figures[-1][1])}</figcaption></figure>')

    def table(self, lines):
        _, caption, widths = lines[0].split("|")
        index = len(self.tables) + 1
        self.tables.append((f"table-{index}", f"Bảng {index}. {caption}"))
        output = [f'<table id="table-{index}"><caption>{self.rich(self.tables[-1][1])}</caption>',
                  "<colgroup>"]
        for width in widths.split(","):
            output.append(f'<col style="width:{float(width) * 100:g}%">')
        output.append("</colgroup><thead>")
        for row_index, line in enumerate(lines[1:]):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if row_index == 0:
                output.append("<tr>" + "".join(f'<th scope="col">{self.rich(cell)}</th>' for cell in cells) + "</tr></thead><tbody>")
            else:
                rendered = [self.rich(cell) for cell in cells]
                if index == 7:
                    rendered[0] = re.sub(r"(?<=[A-Za-z])\.(?=[A-Za-z])", ".<wbr>", rendered[0])
                output.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in rendered) + "</tr>")
        output.append("</tbody></table>")
        return "\n".join(output)

    def references(self):
        entries = []
        for item in self.items:
            year = f", {item['year']}" if item.get("year") else ""
            url = escape(item["url"], quote=True)
            entries.append(f'<li id="ref-{item["id"]}"><span class="ref-index">[{self.ids[item["id"]]}]</span> '
                           f'{escape(item["author"])}, “{escape(item["title"])}”{escape(year)}. '
                           f'[Trực tuyến]. Truy cập 25/11/2026.<br><a href="{url}">{url}</a></li>')
        return '<ol class="references" role="list">' + "\n".join(entries) + "</ol>"

    def chapter(self, path, front=False):
        output = []
        for index, block in enumerate(blocks(path), 1):
            lines = block.splitlines()
            line = lines[0]
            if line.startswith("#"):
                output.append(self.heading(line, path, index, front))
            elif line.startswith("!figure|"):
                output.append(self.figure(line))
            elif line.startswith("!table|"):
                output.append(self.table(lines))
            elif line == "!refs":
                output.append(self.references())
            elif line in ("!toc", "!lof", "!lot"):
                output.append(f"<!-- {line[1:]} -->")
            elif line.startswith("> "):
                sample = "\n".join(item.removeprefix("> ") for item in lines)
                output.append(f"<pre>{self.rich(sample)}</pre>")
            else:
                output.append(f'<p>{self.rich(" ".join(lines))}</p>')
        section = "front" if front else "chapter"
        return f'<section class="{section}">\n' + "\n".join(output) + "\n</section>"

    def build(self):
        front = self.chapter(SOURCE / "00-front.md", front=True)
        main = "\n".join(self.chapter(path) for path in sorted(SOURCE.glob("[1-8][0-9]-*.md")))
        front = front.replace("<!-- toc -->", index_list(self.chapters, "Mục lục"))
        front = front.replace("<!-- lof -->", index_list(self.figures, "Danh mục hình"))
        front = front.replace("<!-- lot -->", index_list(self.tables, "Danh mục bảng"))
        if self.used != set(self.ids):
            raise ValueError("Reference ids in main text differ from bibliography")
        (THESIS / "html" / "index.html").write_text(PAGE.format(front=front, main=main), encoding="utf-8")
        print(f"HTML: {len(self.chapters)} sections, {len(self.figures)} figures, {len(self.tables)} tables, {len(self.items)} references")


def index_list(items, label):
    rows = "\n".join(f'<li><a href="#{anchor}">{escape(title)}</a></li>' for anchor, title in items)
    return f'<nav aria-label="{label}"><ul>{rows}</ul></nav>'


def cover(kind, main=False):
    heading = "h1" if main else "h2"
    return f"""<section class="cover">
    <p>[TÊN TRƯỜNG] · [TÊN KHOA]</p>
    <p>{kind} · Đồ án Chuyên đề ASP.NET</p>
    <{heading}>BA ĐỘNG — Coastal Escape</{heading}>
    <p>Sinh viên thực hiện Lê Hiền<br>Mã số sinh viên 170125405<br>Lớp DK25TTC5</p>
    <p>Giảng viên hướng dẫn [HỌ VÀ TÊN GVHD]<br>Email [EMAIL SINH VIÊN]<br>Điện thoại [SỐ ĐIỆN THOẠI SINH VIÊN]</p>
    <p>[ĐỊA DANH] · 2026<br>Khung trình bày chờ mẫu được xác nhận.</p>
    </section>"""


def review(group):
    return f"""<section class="review">
    <h2>NHẬN XÉT CỦA {group}</h2>
    <p>Đề tài BA ĐỘNG — Coastal Escape<br>Sinh viên Lê Hiền · MSSV 170125405 · Lớp DK25TTC5</p>
    <p>[MẪU NHẬN XÉT CHỜ XÁC NHẬN]<br>[NỘI DUNG DÀNH CHO NGƯỜI NHẬN XÉT]</p>
    </section>"""


PAGE = """<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Luận văn BA ĐỘNG — Coastal Escape</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#document">Đến nội dung luận văn</a>
<header>
  <a href="#top">BA ĐỘNG — Coastal Escape</a>
  <a href="#00-front-4">Mục lục</a>
</header>
<main id="document" tabindex="-1">
<article id="top">
""" + cover("BÌA CHÍNH", main=True) + cover("BÌA PHỤ") + review("GIẢNG VIÊN HƯỚNG DẪN") + review("THÀNH VIÊN HỘI ĐỒNG") + """
{front}
{main}
</article>
</main>
<footer><a href="#top">Về đầu luận văn</a></footer>
</body>
</html>
"""


if __name__ == "__main__":
    HtmlThesis().build()
