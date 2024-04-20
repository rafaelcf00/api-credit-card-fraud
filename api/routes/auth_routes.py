from datetime import timedelta
from ..types.user import UserType
from sqlalchemy.orm import Session
from ..common.find_db import find_user
from ..models.users_model import Users
from passlib.context import CryptContext
from ..models.dependencies import get_db
from ..types.token import OAuth2RequestForm, Token
from fastapi import APIRouter, Depends, HTTPException, status
from ..common.authenticate import create_access_token, verify_password

router = APIRouter(tags=['Auth'])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/auth/register', status_code=200)
async def register_user(data: UserType) -> UserType:
    try:
        if data:
            data.password_hash = pwd_context.hash(data.password_hash)
            user = Users(**data.__dict__)

            if user:
                return user
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
    
@router.post('/auth/login', status_code=200)
async def auth_user(data: OAuth2RequestForm, model: Session = Depends(get_db)) -> Token:
    try:
        user = await find_user(data.email, model)
        if user:
            verify = verify_password(data.password, user.password_hash)

            if verify is False:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid password or email",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            access_token_expires = timedelta(days=2)
            access_token = create_access_token(
                data={'sub': user.email},
                expires_token=access_token_expires
            )

            return Token(
                access_token= access_token,
                token_type='bearer'
            )
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))