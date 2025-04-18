from typing import Any, List, Optional

from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[int]]
    predictions: Optional[int]

class DataInputSchema(BaseModel):
    SIZE: Optional[int]
    FUEL: Optional[str]
    DISTANCE: Optional[int]
    DESIBEL: Optional[int]
    AIRFLOW: Optional[float]
    FREQUENCY: Optional[int]


class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]

