import os
from fastapi import APIRouter, HTTPException
from api.common.convert_csv_json import convert_to_json

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