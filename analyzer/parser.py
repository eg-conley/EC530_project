# parser.py reads the documents (PDF, DOCX, text, etc)
import fitz  # PyMuPDF

def load_document(path):
    ext = path.split(".")[-1]
    if ext == "pdf":
        return extract_text_from_pdf(path)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])
