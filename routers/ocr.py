from fastapi import APIRouter, Depends,UploadFile,File, Form
from services.ocrService import uploadDocument
from config.database import get_db
from sqlalchemy.orm import Session
from schemas import DocumentUpload
ocrRoute = APIRouter()

@ocrRoute.post("/uploadDoc")
async def ocr_document(user_id : str=Form(...),file: UploadFile = File(...)):
    #print(form.keys())  # Check the keys being sent in the request
    #print("gllll"+file.filename)
    print(user_id)
    data = await uploadDocument(user_id,file)
    return data