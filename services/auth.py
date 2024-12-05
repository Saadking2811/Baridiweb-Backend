
from schemas import UserCreate,UserLogin,PasswordResetRequest
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import User
from fastapi import HTTPException, Depends
from utils.jwt import hash_password,verify_password
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    print(user)
    existing_user = db.query(User).filter(User.email == user.email).first()
    print(existing_user)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(email=user.email,fullName=user.fullName,phoneNumber=user.phoneNumber,hashedPassword=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success":True,"message": "User created successfully"}

def findUser(user:UserLogin,db:Session=Depends(get_db)):
    existingUser=db.query(User).filter(User.email==user.email).first()
    print(existingUser.phoneNumber)
    if existingUser:
        if verify_password(user.password,existingUser.hashedPassword):
            #const { password, ...userDataWithoutPassword } = existingUser;
            # change status to active 
            existingUser.isActive=True
            db.commit()
            db.refresh(existingUser)
            return {"success":True,"userData":existingUser}
        else:
            raise HTTPException(status_code=400,detail="Invalid password")
    else:
        raise HTTPException(status_code=400,detail="User not found")
    

def forgetPassword(email:PasswordResetRequest,db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(User.email==email.email).first()
    if existing_user:
        # Send password reset email
        return {"message": "Password reset email sent successfully"}
    else:   
        raise HTTPException(status_code=400,detail="User not found")



def showProfile(user_id:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user_data = user.__dict__.copy()
        user_data.pop('hashedPassword', None)
        return user_data
    else:
        raise HTTPException(status_code=404, detail="User not found")