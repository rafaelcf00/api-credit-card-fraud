import os
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from api.common.convert_csv_json import convert_to_json
from api.models.dependencies import get_db
from api.models.inputs_model import Inputs
from api.types.input import InputMobileType, ResponseDatasetType

router = APIRouter(tags=['Dataset'])

directory = 'dataset/'
filename = 'new_fraud_dataset.csv'

@router.get('/{filename}', status_code=200)
async def export_json():
    csv_path = os.path.join(directory, filename)
    try:
        if csv_path:
            json_dataset = convert_to_json(csv_path)
            return json_dataset
        else:
            raise HTTPException(status_code=404, detail='File not found.')
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))


@router.post('/input', status_code=201)
async def insert_in_dataset(data: InputMobileType, db: Session = Depends(get_db)) -> InputMobileType:
    try:
        if data:
            insert = Inputs(**data.__dict__)

            if insert:
                db.add(insert)
                db.commit()
                db.refresh(insert)

                return insert
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))

@router.get('/input', response_model=List[InputMobileType], status_code=200)
async def find_input(db: Session = Depends(get_db)) -> InputMobileType:
    try:
        inputs = db.query(Inputs).all()
        print(inputs)
        if len(inputs) != 0:
            return inputs
        else:
            raise HTTPException(status_code=404, detail='Input not found.')
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))

@router.get('/input/{id}', response_model=InputMobileType, status_code=200)
async def get_input(id: int, db: Session = Depends(get_db)) -> InputMobileType:
    try:
        input = db.query(Inputs).filter_by(id= id).first()

        if input:
            return input
        else:
            raise HTTPException(status_code=404, detail='Input not found.')
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))

@router.post('/response-dataset', status_code=201)
async def return_response(data: ResponseDatasetType, Session = Depends(get_db)) -> ResponseDatasetType:
    try:
        if data:
            return data
    except Exception as error:
        HTTPException(status_code=500, detail=str(error))