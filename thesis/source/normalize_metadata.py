"""Set handoff metadata without assigning editorial work to the author."""

from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from pypdf import PdfReader, PdfWriter


THESIS = Path(__file__).resolve().parent.parent
AUTHOR = "Lê Hiền"
TITLE = "BA ĐỘNG — Coastal Escape"
SUBJECT = "Đồ án Chuyên đề ASP.NET"
SLIDE_TITLE = f"{TITLE} — Báo cáo bảo vệ"
CORE = "docProps/core.xml"
DC = "http://purl.org/dc/elements/1.1/"
CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"


def save(path, payload):
    with NamedTemporaryFile(dir=path.parent, suffix=".tmp", delete=False) as scratch:
        scratch_path = Path(scratch.name)
    try:
        scratch_path.write_bytes(payload)
        scratch_path.replace(path)
    finally:
        scratch_path.unlink(missing_ok=True)


def normalize_office(path, title):
    result = BytesIO()
    with ZipFile(path) as original:
        core = ET.fromstring(original.read(CORE))
        values = {
            f"{{{DC}}}creator": AUTHOR,
            f"{{{DC}}}title": title,
            f"{{{DC}}}subject": SUBJECT,
            f"{{{CP}}}lastModifiedBy": "",
        }
        for tag, value in values.items():
            node = core.find(tag)
            if node is None:
                node = ET.SubElement(core, tag)
            node.text = value
        ET.register_namespace("cp", CP)
        ET.register_namespace("dc", DC)
        ET.register_namespace("dcterms", "http://purl.org/dc/terms/")
        with ZipFile(result, "w") as normalized:
            for entry in original.infolist():
                payload = ET.tostring(core, encoding="utf-8", xml_declaration=True) if entry.filename == CORE else original.read(entry)
                normalized.writestr(entry, payload)
    save(path, result.getvalue())


def normalize_pdf(path, title):
    reader = PdfReader(path)
    current = reader.metadata or {}
    xmp = reader.xmp_metadata
    values = {"/Title": title, "/Author": AUTHOR, "/Subject": SUBJECT}
    if (all(current.get(key) == value for key, value in values.items()) and xmp
            and xmp.dc_title.get("x-default") == title and xmp.dc_creator == [AUTHOR]
            and xmp.dc_description.get("x-default") == SUBJECT):
        return
    writer = PdfWriter(clone_from=reader)
    writer.add_metadata(values)
    xmp = writer.xmp_metadata
    if xmp:
        xmp.dc_title = {"x-default": title}
        xmp.dc_creator = [AUTHOR]
        xmp.dc_description = {"x-default": SUBJECT}
    result = BytesIO()
    writer.write(result)
    save(path, result.getvalue())


if __name__ == "__main__":
    normalize_office(THESIS / "doc/BA-DONG-Coastal-Escape.docx", TITLE)
    normalize_office(THESIS / "abs/BA-DONG-Coastal-Escape.pptx", SLIDE_TITLE)
    normalize_pdf(THESIS / "pdf/BA-DONG-Coastal-Escape.pdf", TITLE)
    normalize_pdf(THESIS / "abs/BA-DONG-Coastal-Escape-Slides.pdf", SLIDE_TITLE)
