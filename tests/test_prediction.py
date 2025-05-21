
import pytest
from fastapi.testclient import TestClient
from prediction_service.main import app

client = TestClient(app)

def test_predict():
    response = client.get("/predict/123")
    assert response.status_code == 200
    assert "risk_score" in response.json()
    