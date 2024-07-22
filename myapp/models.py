from django.db import models

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_cancer_seins.pkl')
scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/scaler_cancer_seins.pkl')

def preprocess(data):
    data_scaled = scaler.transform(data)
    return data_scaled

def predict(data):
    data_preprocessed = preprocess(data)
    prediction = model.predict(data_preprocessed)
    return prediction