import fitz
def ExtractPDFText(pdf_path):
    content = ""
    pdf_document = fitz.open(pdf_path)
    for page_number in range(pdf_document.page_count):
        # Get the text content of the page
        page = pdf_document[page_number]
        text = page.get_text()
        content += text 


    pdf_document.close()
    return content 