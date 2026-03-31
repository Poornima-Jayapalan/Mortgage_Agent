def extract_with_ocr(tmp_path):
    try:
        import pytesseract
        from pdf2image import convert_from_path
        from langchain_core.documents import Document

        images = convert_from_path(tmp_path)
        pages = []

        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            pages.append(Document(page_content=text, metadata={"page": i}))

        return pages

    except ImportError:
        return []
