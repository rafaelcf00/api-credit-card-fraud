from sqlalchemy.orm import Session
from ..models.users_model import Users
from fastapi import HTTPException, status

async def find_user(email: str, model: Session):
    response = model.query(Users).filter_by(email= email).first()
    if response:
        return response
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail='User not found')