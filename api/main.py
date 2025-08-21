import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="Heart Disease Prediction API", version="0.1.0")

# Pydantic schema
class HeartFeatures(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Load the latest model
def _latest_model_path():
    models_dir = os.path.join(os.path.dirname(__file__), "../models")
    model_files = [f for f in os.listdir(models_dir) if f.endswith(".pkl")]
    if not model_files:
        raise FileNotFoundError("No model found. Train a model in ./models first.")
    latest_model = max(model_files, key=lambda x: os.path.getmtime(os.path.join(models_dir, x)))
    return os.path.join(models_dir, latest_model)

MODEL_PATH = _latest_model_path()
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(features: HeartFeatures):
    # Convert input to DataFrame with proper column names
    X = pd.DataFrame([features.dict()])
    
    # Predict
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]  # probability of positive class

    return {"prediction": int(prediction), "probability": float(probability)}
