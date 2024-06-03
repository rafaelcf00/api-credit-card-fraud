from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.models.dependencies import get_db
from api.models.fraud_model import Frauds
from api.models.inputs_model import Inputs
from api.types.fraud import ResponseDatasetType


router = APIRouter(tags=['Fraud'])

@router.post('', status_code=201)
async def insert_reponse_input(data: ResponseDatasetType, db: Session = Depends(get_db)) -> ResponseDatasetType:
    try:
        if data:
            input = db.query(Inputs).filter_by(id= data.input_id).first()
            if input:
                is_fraud = Frauds(**data.__dict__)
                if is_fraud:
                    db.add(is_fraud)
                    db.commit()
                    db.refresh(is_fraud)

                    return is_fraud
            else:
                HTTPException(status_code=404, detail='Input not found')
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))

@router.get(
    '/{id}', 
    response_model=ResponseDatasetType,
    response_model_exclude=['input_id'],
    status_code=200
)
async def find_response_input(id: int, db: Session = Depends(get_db)) -> ResponseDatasetType:
    try:
        is_fraud = db.query(Frauds).filter_by(id= id).first()
        if is_fraud:
            return is_fraud
        else:
            HTTPException(status_code=404, detail='Response not found')
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))