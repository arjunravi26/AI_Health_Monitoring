
import pandas as pd

def merge_data(wearable_df, lab_df):
    return pd.merge_asof(
        wearable_df.sort_values('timestamp'),
        lab_df.sort_values('date'),
        left_on='timestamp',
        right_on='date',
        by='patient_id',
        direction='backward'
    )
    