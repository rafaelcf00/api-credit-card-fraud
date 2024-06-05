from typing import Optional
from pydantic import BaseModel


class ResponseDatasetType(BaseModel):
    id: Optional[int] = None
    is_fraud: int
    input_id: int
