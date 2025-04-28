# tests made with ChatGPT and modified
# parser.py tests

# python -m coverage run -m pytest -s
# python coverage report -m

import pytest
import fitz  # PyMuPDF
import docx # python-docx for DOCX

from autoteacherai.analyzer.parser import *

def test_load_document_pdf(tmp_path):
    pdf_path = tmp_path / "test.pdf"
    content = "This is a PDF file."

    # create a temporary PDF file using PyMuPDF
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), content)
    doc.save(pdf_path)
    doc.close()

    # verify
    extracted = load_document(str(pdf_path))
    assert content in extract_text_from_pdf(str(pdf_path))
    assert content in extracted

def test_load_document_docx(tmp_path):
    docx_path = tmp_path / "test.docx"
    content = "This is a DOCX file."

    # create DOCX file
    doc = docx.Document()
    doc.add_paragraph(content)
    doc.save(docx_path)

    # verify
    assert load_document(str(docx_path)) == content
    assert extract_text_from_docx(str(docx_path)) == content

def test_load_document_txt(tmp_path):
    content = "This is a txt file."
    txt_path = tmp_path / "test.txt"

    # create txt file
    txt_path.write_text(content)

    # verify
    assert load_document(str(txt_path)) == content
    assert extract_text_from_txt(str(txt_path)) == content

def test_load_unsupported_file(tmp_path):
    fake_path = tmp_path / "test.xyz"
    fake_path.write_text("some data")

    with pytest.raises(ValueError, match=r"Unsupported file extension.*"):
        load_document(str(fake_path))