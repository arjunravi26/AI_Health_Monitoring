
import xgboost as xgb

def load_model():
    model = xgb.XGBClassifier()
    model.load_model('model.json')
    return model
    