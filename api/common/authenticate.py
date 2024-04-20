import os
import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone

def verify_password(password: str, hashed_password: bytes):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(password, hashed_password) 

def create_access_token(data: dict, expires_token: timedelta | None = None):
    algorithm = os.getenv('ALGORITHM')
    secret_key = os.getenv('SECRET_KEY')

    to_encoded = data.copy()
    if expires_token:
        expire = datetime.now(timezone.utc) + expires_token
    else:
        expire = datetime.now(timezone.utc) + timedelta(days=2)
    to_encoded.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encoded, str(secret_key), algorithm=algorithm)
    return encoded_jwt