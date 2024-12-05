from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta


SECRET_KEY = "b1e7"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(enteredPass:str,hashedPassword)->bool:
    return pwd_context.verify(enteredPass,hashedPassword)


# Generate and verify JWT tokens
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
