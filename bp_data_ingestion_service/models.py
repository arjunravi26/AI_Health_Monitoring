
from pydantic import BaseModel

class WearableData(BaseModel):
    patient_id: str
    timestamp: str
    device_type: str
    value: float

class LabData(BaseModel):
    patient_id: str
    date: str
    test_type: str
    result: float