from sqlalchemy.orm import Session
from ..models.users_model import Users
from passlib.context import CryptContext
from ..models.dependencies import get_db
from ..types.user import UserType, UserUpdateType
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(tags=['Users'])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def user_by_id(id: int, model: Session):
    response = model.query(Users).filter_by(id= id).first()
    if response:
        return response
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='User not found') 

@router.get(
    '/{id}',
    response_model=UserType, 
    response_model_exclude=['password_hash'],
    status_code=200
)
async def find_user(id: int, model: Session = Depends(get_db)) -> UserType:
    try:
        user = await user_by_id(id, model)
        if user:
            return user
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

@router.put(
    '/{id}', 
    response_model=UserUpdateType, 
    status_code=200
)
async def update_user(id: int, data: UserUpdateType, model: Session = Depends(get_db)) -> UserUpdateType:
    try:
        if data:
            user = await user_by_id(id, model)
            if data.password_hash:
                data.password_hash = pwd_context.hash(data.password_hash)
            if user:
                for attr in vars(user):
                    if hasattr(data, attr):
                        setattr(user, attr, getattr(data, attr))
                
                model.commit()
                model.refresh(user)

                return user
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))