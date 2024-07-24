from django.db import models

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

cancer_model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_cancer_seins.pkl')
cardiac_model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_heart_disease.pkl')
diabetes_model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_diabetes_std.pkl')
foie_model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_foie2.pkl')
renal_model = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/model_reins2.pkl')

cancer_scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/scaler_cancer_seins.pkl')
cardiac_scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/scaler_heart_disease.pkl')
diabetes_scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/Scaler_diab.pkl')
foie_scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/scaler_foie2.pkl')
renal_scaler = joblib.load('/Users/lua/wild/project3/wlab_backend/myapp/scaler_reins2.pkl')


def preprocess(data, scaler):
    data_scaled = scaler.transform(data)
    return data_scaled

def predict_cancer(data):
    data_preprocessed = preprocess(data, cancer_scaler)
    prediction = cancer_model.predict(data_preprocessed)
    return 'Bénigne' if prediction[0] == 0 else 'Maligne'

def predict_cardiac(data):
    data_preprocessed = preprocess(data, cardiac_scaler)
    prediction = cardiac_model.predict(data_preprocessed)
    return 'Négatif' if prediction[0] == 0 else 'Positif'

def predict_diabetes(data):
    data_preprocessed = preprocess(data, diabetes_scaler)
    prediction = diabetes_model.predict(data_preprocessed)
    return 'Négatif' if prediction[0] == 0 else 'Positif'

def predict_foie(data):
    data_preprocessed = preprocess(data, foie_scaler)
    prediction = foie_model.predict(data_preprocessed)
    return prediction[0]

def predict_renal(data):
    data_preprocessed = preprocess(data, renal_scaler)
    prediction = renal_model.predict(data_preprocessed)
    return prediction[0]


