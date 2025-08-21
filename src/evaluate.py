# src/evaluate.py

import pandas as pd
import joblib
from src.config import FEATURES, TARGET

DATA_PATH = "data/processed_heart.csv"
MODEL_PATH = "models/heart_model.pkl"

def evaluate():
    print(f"Evaluating model using features: {FEATURES} and target: {TARGET}")

    # Load data
    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]
    y = df[TARGET]

    # Load model
    model = joblib.load(MODEL_PATH)
    score = model.score(X, y)
    print(f"Evaluation accuracy on full dataset: {score}")

if __name__ == "__main__":
    evaluate()
