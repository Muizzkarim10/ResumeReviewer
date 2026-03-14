from io import BytesIO
from pypdf import pdfReader

def extract_text_from_pdf(pdf_bytres: bytes) -> str:
    try:
        reader = pdfReader(BytesIO(pdf_bytres))

        if reader.is_encrypted:
            raise ValueError("This pdf is password-protected.")

        pages_text = [
            page.extract_text() or ""
            for page in reader.pages
        ]

        extracted_text = "\n".join(pages_text).strip()

    except ValueError:
        raise

    except Exception as e:
        raise ValueError("We could not read this Pdf file.") from error
    

    if not extracted_text:
        raise ValueError(
            "No selectable text was found in this Pdf file."
            "A scanned resume will need OCR support later"
            )
