
import pandas as pd
import numpy as np

# Wearable data
dates = pd.date_range(start='2023-10-01', end='2023-10-07', freq='H')
wearable_df = pd.DataFrame({
    'patient_id': ['123'] * len(dates),
    'timestamp': dates,
    'device_type': ['glucose'] * len(dates),
    'value': np.clip(np.random.normal(loc=100, scale=20, size=len(dates)), 50, 200)
})
wearable_df.to_csv('data/wearable_data.csv', index=False)

# Lab data
lab_dates = pd.date_range(start='2023-10-01', end='2023-10-07', freq='14D')
lab_df = pd.DataFrame({
    'patient_id': ['123'] * len(lab_dates),
    'date': lab_dates,
    'test_type': ['HbA1c'] * len(lab_dates),
    'result': [6.2, 6.5]
})
lab_df.to_csv('data/lab_data.csv', index=False)
    