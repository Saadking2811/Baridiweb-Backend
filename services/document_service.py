from sqlalchemy.orm import Session
from config.database import get_db
from schemas import DocumentUpload
from models.models import Document,IDCard,Check,CheckSecours
from fastapi import Depends

def createDoc(userId:int,data,docType:str,filePath:str,db:Session=Depends(get_db)):
    document = Document(owner_id=userId,filePath=filePath,docType=docType,title=data["title"] | "")
    if(docType=="check"):
        createCheck(data,document)
    elif(docType=="idCard"):
        createIDCardDocument(data,document)
    else:
        createCheckSecours(data,document)




def createCheck(data,document:Document):
    check = Check(id=document.id,check_number=data.check_number,amountInText=data.amountInText,amountInDigits=data.amountInDigits)
    


def createIDCardDocument(data,document:Document):
    cardId = IDCard(id=document.id,idNumber=data.idNumber,firstName=data.firstName,lastName=data.lastName,issueDate=data.issueDate)
    
def createCheckSecours(data,document:Document):
    checksecours = CheckSecours(id=document.id,amountInDigits=data.amountInDigits,amountInText=data.amountInText,senderFirstName=data.senderFirstName,senderLastName=data.senderLastName,receiverFirstName=data.receiverFirstName,receiverLastName=data.receiverLastName,receiverCle=data.receiverCle,receiverCCP=data.receiverCCP)
    