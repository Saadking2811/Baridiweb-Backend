from utils.random import generate_ccp_code,generate_cle
from sqlalchemy.orm import Session
from models.models import User
from config.database import get_db
from fastapi import HTTPException, Depends,status
def create_account(user_id:int,db: Session = Depends(get_db)):
    ccp_code = generate_ccp_code
    cle = generate_cle
    # save the account

    user = db.query(User).filter(User.id == user_id).first()

    # If the user doesn't exist, raise a 404 error
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.ccp=ccp_code
    user.cle=cle

    # Commit the changes to the database
    db.commit()

    # Refresh the user object to reflect the updated data
    db.refresh(user)

    return user

