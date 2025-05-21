
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

# Placeholder: Replace with your data
df = pd.read_csv('data/merged_data.csv')
X = df[['value', 'result']]
y = df['risk_label']  # Assume labels exist
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = xgb.XGBClassifier()
model.fit(X_train, y_train)
model.save_model('prediction_service/model.json')
    