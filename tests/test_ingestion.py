
import pytest
from fastapi.testclient import TestClient
from data_ingestion_service.main import app

client = TestClient(app)

def test_ingest_wearable():
    response = client.post("/ingest/wearable", json={
        "patient_id": "123",
        "timestamp": "2023-10-01T00:00:00",
        "device_type": "glucose",
        "value": 100.0
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    