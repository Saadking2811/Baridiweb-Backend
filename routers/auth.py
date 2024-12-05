from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.auth import createUser,findUser,forgetPassword,showProfile
from schemas import UserCreate, PasswordResetRequest,UserLogin,UserProfile
from config.database import get_db

authRouter = APIRouter()

# POST method with correct URL path
@authRouter.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):  # Make sure to pass db as a dependency here
    return createUser(user, db)  # Pass db to createUser function


@authRouter.post("/login")
def register(user: UserLogin, db: Session = Depends(get_db)):  # Make sure to pass db as a dependency here
    return findUser(user, db)  # Pass db to createUser function


@authRouter.post("/forgetPassword")
def register(user: PasswordResetRequest, db: Session = Depends(get_db)):  # Make sure to pass db as a dependency here
    return forgetPassword(user, db)  # Pass db to createUser function


@authRouter.post("/profile")
def getProfile(data : UserProfile,db: Session = Depends(get_db)):
    return showProfile(data.user_id,db)