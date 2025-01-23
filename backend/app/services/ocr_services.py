import base64
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
import io

async def process_pdf(file) -> str:
    """
    Processes a base64-encoded PDF to extract text.

    Args:
        pdf_base64 (str): Base64 encoded string of the PDF.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        # Decode the base64 PDF
        file_bytes = await file.read()
        
        # Encode the file content to base64
        pdf_base64 = base64.b64encode(file_bytes).decode("utf-8")
        
        pdf_content = base64.b64decode(pdf_base64)

        # Load the PDF content into a PyPDF2 reader
        pdf_stream = io.BytesIO(pdf_content)
        reader = PdfReader(pdf_stream)

        # Extract text from all pages
        document_text = ""
        for page in reader.pages:
            document_text += page.extract_text()

        return document_text.strip()

    except Exception as e:
        print(f"Error processing PDF: {e}")
        raise e


async def process_image(image_base64: str) -> str:
    """
    Processes a base64-encoded image to extract text.

    Args:
        image_base64 (str): Base64 encoded string of the image.

    Returns:
        str: Extracted text from the image.
    """
    try:
        # Decode the base64 image
        image_content = base64.b64decode(image_base64)

        # Open the image using PIL
        image = Image.open(io.BytesIO(image_content))

        # Extract text using pytesseract
        document_text = pytesseract.image_to_string(image)

        return document_text.strip()

    except Exception as e:
        print(f"Error processing image: {e}")
        raise e


async def process_file(file_path: str) -> str:
    """
    Processes a file (PDF or image) to extract text.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Extracted text from the file.
    """
    try:
        # Read the file and encode it to base64
        with open(file_path, "rb") as f:
            file_content = base64.b64encode(f.read()).decode("utf-8")

        # Determine the file type and process accordingly
        if file_path.endswith(".pdf"):
            return await process_pdf(file_content)
        elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
            return await process_image(file_content)
        else:
            return "Unsupported file type. Please upload a PDF or image."

    except Exception as e:
        print(f"Error processing file: {e}")
        raise e


if __name__ == "__main__":
    import asyncio

    # Example Usage
    file_path = "C:/Users/alexm/Downloads/Deepak Singh CV-5.pdf"
    if not os.path.exists(file_path):
        print("File not found. Please check the path and try again.")
    else:
        # Run the async function to process the file
        extracted_text = asyncio.run(process_file(file_path))
        print("Extracted Text:\n", extracted_text)
