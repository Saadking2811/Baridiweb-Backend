from pydantic import BaseModel,EmailStr
from typing import List, Optional


class UserCreate(BaseModel):
    email:EmailStr
    password:str
    isAdmin:bool
    fullName:str
    phoneNumber:str

class UserLogin(BaseModel):
    email:EmailStr
    password: str

class UserProfile(BaseModel):
    user_id :int

class PasswordResetRequest(BaseModel):
    email: EmailStr

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str

class DocumentUpload(BaseModel):
    user_id: int

