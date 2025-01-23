import base64
from ocr_services import process_pdf
import os
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_text_from_image(image_path):
    """Extract text from a handwritten note (image)."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error reading image: {e}"

def process_file(file_path):
    """Process a file (PDF or image) and return the extracted text."""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        return extract_text_from_image(file_path)
    else:
        return "Unsupported file type. Please upload a PDF or image."

if __name__ == "__main__":
    # Example Usage
    file_path = "C:/Users/alexm/Downloads/Deepak Singh CV-5.pdf"
    if os.path.exists(file_path):
        result = process_file(file_path)
        print("Extracted Text:\n", result)
    else:
        print("File not found. Please check the path and try again.")

# async def main():
#     # Example: Encoding a PDF file to base64
#     with open("C:/Users/alexm/Downloads/Deepak Singh CV-5.pdf", "rb") as f:
#         pdf_content = base64.b64encode(f.read()).decode("utf-8")
    
#     # Call the asynchronous function
#     text = await process_pdf(pdf_content)
#     print(text)

# Run the async main function
# import asyncio
# asyncio.run(main())
