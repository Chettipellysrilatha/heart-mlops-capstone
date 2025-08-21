import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

# Load processed data
data = pd.read_csv("data/processed_heart.csv")

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]
TARGET = "target"

X = data[FEATURES]
y = data[TARGET]

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
with open("models/heart_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
roc = roc_auc_score(y_test, y_pred)

print(f"Model saved to models/heart_model.pkl")
print(f"Metrics - Acc: {acc:.3f}, ROC-AUC: {roc:.3f}")