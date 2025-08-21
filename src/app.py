# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import time
import logging

# Logging setup
logging.basicConfig(filename="logs/predictions.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Load model
MODEL_PATH = "models/heart_model.pkl"
model = joblib.load(MODEL_PATH)

# Feature names
FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]

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

app = FastAPI(title="Heart Disease Prediction API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "OK", "model_version": "v1"}

@app.post("/predict")
def predict(features: HeartFeatures):
    start_time = time.time()

    # Convert input to DataFrame
    data = pd.DataFrame([features.dict()])[FEATURES]
    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    latency = time.time() - start_time

    # Logging
    logging.info({
        "input": features.dict(),
        "prediction": int(pred),
        "probability": float(prob),
        "latency": latency
    })

    return {"prediction": int(pred), "probability": float(prob)}
