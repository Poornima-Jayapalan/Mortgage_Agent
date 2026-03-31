"""
Test OCR extraction using Tesseract.
Place a scanned PDF in sample_docs/scanned.pdf
"""

from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

pdf_path = Path("sample_docs/scanned.pdf")

if not pdf_path.exists():
    raise FileNotFoundError("Place a scanned PDF at sample_docs/scanned.pdf")

print("Converting PDF to images...")
images = convert_from_path(str(pdf_path))

print("Running OCR...")
text = ""
for img in images:
    text += pytesseract.image_to_string(img)

print("\n=== OCR OUTPUT (first 1000 chars) ===\n")
print(text[:1000])
