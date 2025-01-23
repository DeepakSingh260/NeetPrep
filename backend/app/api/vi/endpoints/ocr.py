from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.ocr_services import process_pdf
from app.services.save_pdf_services import save_extracted_text_to_firebase
import re
router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    extracted_text = await process_pdf(file)
    formatted_text = re.sub(r"(?<!\n)\n(?!\n)", " ", extracted_text)

    formatted_text = re.sub(r"\s{2,}", " ", formatted_text)

    formatted_text = formatted_text.strip()
    document_id = await save_extracted_text_to_firebase("testId",formatted_text)
    return {
        "message": "PDF processed and saved successfully",
        "document_id": document_id,
        "formatted_text": formatted_text[:100]+"....."
    }
