from models.models import User
from sqlalchemy.orm import Session

from fastapi import HTTPException, Depends
from config.database import get_db
def getReceiverInfo(ccp: str,db: Session = Depends(get_db)):
    receiver = db.query(User).filter(User.ccp == ccp).first()
    if receiver:
        return {"receiver_fullname": receiver.fullName}
    else:
        return None



def get_sender_info(ccp:str,db:Session= Depends(get_db)):
    sender = db.query(User).filter(User.ccp==ccp).first()
    if sender:
        return {"receiver_fullname": sender.fullName}
    else:
        return None