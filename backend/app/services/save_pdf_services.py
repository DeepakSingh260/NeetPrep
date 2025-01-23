import uuid
import firebase_admin
from firebase_admin import credentials  
from fastapi import UploadFile
from google.cloud import firestore
from google.oauth2 import service_account
# Initialize Firebase
cred = service_account.Credentials.from_service_account_file("serviceAccountKey.json")


db = firestore.Client(credentials=cred,database="neetprepdatabaseid")

async def save_extracted_text_to_firebase(user_id: str, extracted_text: str) -> str:
    """
    Saves the extracted text to Firebase Firestore with a unique UUID as the document ID, including a user ID.

    Args:
        user_id (str): The ID of the user.
        extracted_text (str): The text extracted from the PDF.

    Returns:
        str: The generated document ID.
    """
    try:
        document_id = str(uuid.uuid4())

        data = {
            "user_id": user_id,
            "document_id": document_id,
            "extracted_text": extracted_text,
            "timestamp": firestore.SERVER_TIMESTAMP  # Add a timestamp
        }
        
        doc_ref = db.collection("documents").document(document_id)
        doc_ref.set(data)

        return document_id
    except Exception as e:
        print(f"Error saving extracted text to Firebase: {e}")
        raise e