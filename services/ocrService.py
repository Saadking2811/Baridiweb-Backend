import os
from fastapi import UploadFile, HTTPException, File
import shutil
from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from services.user import getReceiverInfo,get_sender_info
from services.document_service import createDoc
# Upload folder configuration
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}
#Helper function to check if the file is allowed
def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def uploadDocument(user_id: int, file: UploadFile = File(...),db:Session=Depends(get_db)):
    print(file.filename)
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")
    else:
        # Create path to store the file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        # Simulating processing (replace with your actual processing logic)
        result = await process_file(file_path)  # Simulating an async file processing function

        if result["success"]:  # Assuming result is a dictionary with "success" as a key
            extracted_data = {
                "docType": "Card_id",
                "firstName": "Hassane",
                "lastName": "BENCHAREF",
                "id_number": "2009283648733",
                "issue_date": "2022-08-11",
                "docType":"check"
            }
            if extracted_data["docType"] == "checkSecours":
                result = await check_receiver_matching(extracted_data)  # Assuming async function
                if not result["error"]:
                    return {"success": True, "extracted_data": extracted_data}
                else:
                    raise HTTPException(status_code=400, detail=result)
            elif extracted_data["docType"]=="check":
                result = await check_sender(extracted_data)  # Assuming async function
                if result["success"]:
                    return {"success": True, "extracted_data": extracted_data}
                else:
                    raise HTTPException(status_code=400, detail=result)
            ## save document to database
            createDoc(user_id,extracted_data,extracted_data["docType"],file_path,db)
        return {"success": False, "detail": "Error processing file"}

# Example of async processing function
async def process_file(file_path: str):
    # Simulate async processing, you can replace this with your actual logic
    return {"success": True}



def check_receiver_matching(extracted_data):
    cle=extracted_data.cle | ""
    ccp=extracted_data.ccp | ""

    # Check if the receiver matches
    if cle and ccp:
        # Check if the receiver is the same
        receiver_info = getReceiverInfo(ccp)
        if receiver_info and receiver_info["ccp"] == ccp:
            return {"error": False, "review": extracted_data}
        else:
            return {"error": True, "review": extracted_data, "message": "ccp entered doesn't match the receiver"}
    else:
        return {"error": True, "review": extracted_data, "message": "Cle and Ccp are required"}


def check_sender(extracted_data):
    errors = []
    cle=extracted_data.sender_cle | ""
    ccp=extracted_data.ccp_sender | ""

    # get sender info from DB 
    sender = get_sender_info(ccp)
    firstNC,lastNC=sender.split(" ")
    firstName=extracted_data.first_name # cardID
    lastName=extracted_data.last_name # cardID

    firstName_c=extracted_data.first_name_c 
    lastName_c=extracted_data.last_name_c
    # Check if the sender matches
    if firstName==firstName_c and lastName==lastName_c and lastName_c==lastName_c and firstNC==firstName and lastNC==lastName :
        return {"success":True,"data":extracted_data}
    if(firstNC != firstName or lastNC != lastName):
        errors.append("entered ccp is not yours !")
        #return {"error":True,"message":"entered ccp is not yours !"}
    if (firstName_c!=firstName or lastName_c!=lastName):
        #return {"error":True,"message":"entered name is not yours !"}
        errors.append("entered name is not yours !")
    return errors