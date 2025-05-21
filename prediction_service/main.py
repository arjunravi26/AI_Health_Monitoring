
from fastapi import FastAPI
import pandas as pd
import xgboost as xgb
from sqlalchemy import create_engine
from shared.database import get_db_connection
from shared.utils import merge_data

app = FastAPI()
model = xgb.XGBClassifier()
model.load_model('model.json')

@app.get("/predict/{patient_id}")
async def predict(patient_id: str):
    engine = get_db_connection()
    wearable_df = pd.read_sql(f"SELECT * FROM wearable_data WHERE patient_id = '{patient_id}'", engine)
    lab_df = pd.read_sql(f"SELECT * FROM lab_data WHERE patient_id = '{patient_id}'", engine)
    merged_df = merge_data(wearable_df, lab_df)
    features = merged_df[['value', 'result']].fillna(0)
    prediction = model.predict_proba(features)[:, 1].mean()
    return {"patient_id": patient_id, "risk_score": float(prediction)}
    