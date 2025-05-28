import fitz  # PyMuPDF
import io

def extract_appraisal_date(file_bytes: bytes):
    doc = fitz.open("pdf", file_bytes)
    results = []

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text()
        if "Appraisal Date" in text:
            blocks = page.search_for("Appraisal Date")
            for b in blocks:
                highlight_text = page.get_textbox(b)
                results.append({
                    "page": page_number,
                    "text": highlight_text,
                    "highlight": {
                        "x": b.x0, "y": b.y0, "width": b.width, "height": b.height
                    }
                })

    return results
