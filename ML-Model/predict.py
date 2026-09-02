import joblib 
import pandas as pd
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print("Loaded the Model")

def make_prediction(data: dict) -> float:
    feature_columns = [
        'longitude',
        'latitude',
        'housing_median_age',
        'total_rooms',
        'total_bedrooms',
        'population',
        'households',
        'median_income',
    ]
    features = pd.DataFrame([[data[column] for column in feature_columns]], columns=feature_columns)
    return saved_model.predict(features)[0]

def batch_predictions(data: List[dict]) -> np.ndarray:
    feature_columns = [
        'longitude',
        'latitude',
        'housing_median_age',
        'total_rooms',
        'total_bedrooms',
        'population',
        'households',
        'median_income',
    ]
    X = pd.DataFrame(
        [[item[column] for column in feature_columns] for item in data],
        columns=feature_columns,
    )
    return saved_model.predict(X)
