# Heart Disease Prediction - MLOps Capstone Project
## Project Overview

This project demonstrates a complete ML workflow for predicting heart disease, from **data preparation** and **MLOPS model training** to **serving predictions via API** with **containerization Docker** and **CI/CD**.

---

## Features

* Clean & preprocess heart disease dataset (`prep_data.py`)
* Train ML models (Logistic Regression, Random Forest, XGBoost) (`train.py`)
* Evaluate models and save metrics (`evaluate.py`)
* Serve predictions via FastAPI (`api/main.py`)
* Validate API inputs with Pydantic schemas (`api/schemas.py`)
* Dockerized API for deployment
* Logging of requests, predictions, and latency in **logs file**
* CI/CD workflow with GitHub Actions (`.github/workflows/ci.yml`)

---

## Project Structure

heart-mlops-capstone/
│
├── data/
│ ├── heart.csv # Raw dataset
│ └── processed_heart.csv # Cleaned & processed dataset
│
├── src/ # Core scripts
│ ├── init.py
│ ├── prep_data.py # Data preprocessing
│ ├── train.py # Train models
│ ├── evaluate.py # Evaluate models
│ └── utils.py # Helper functions
│
├── api/ # API related files
│ ├── main.py # FastAPI app
│ └── schemas.py # Pydantic schemas for input validation
│
├── tests/ # Unit or integration tests
│ └── <test_scripts>.py
│
├── logs/ # Logs for API requests/predictions
│ └── <log_files>.log
│
├── models/ # Saved ML models
│ └── <trained_model_files>
│
├── samples/ # Sample requests or sample data
│ └── <sample_files>
│
├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions workflow for Docker CI/CD
│
├── test_api.py # Script to test the API
├── Dockerfile # Docker image setup
├── .dockerignore
├── .gitignore
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---
## 1. Setup & Installation

### Clone the Repository

```bash
git clone <https://github.com/Chettipellysrilatha/heart-mlops-capstone.git>
cd heart-mlops-capstone
```

### Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Data Preparation

Clean and preprocess the dataset:

```bash
python -m src.prep_data
```

* Input: `data/heart.csv`
* Output: `data/processed_heart.csv`

---

## 3. Model Training

Train models and save the best model:

```bash
python -m src.train
```

* Model saved in `models/model.pkl`
* algorithm: Logistic Regression (can modify `train.py` to try RandomForest or XGBoost)

---

## 4. Model Evaluation

Evaluate the trained model:

```bash
python -m src.evaluate
```

* Computes metrics: Accuracy, ROC-AUC, Precision, Recall
* Displays feature importance

---

## 5. API Service

The FastAPI service allows serving predictions.

### Run the API

```bash
uvicorn api.main:app --reload
```

### Endpoints

1. **Health Check**

   ```
   GET /health
   ```

   Returns `{"status": "ok"}`

2. **Predict Heart Disease**

   ```
   POST /predict
   ----
   POST/docs

   **Body Example:**

```json
{
  "age": 63,
  "sex": 1,
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

**Response:**

```json
{
  "prediction": 0, 
  "probability": 0.235
}
```

---

## 6. Testing the API

You can test the API using the provided `test_api.py`:

```bash
python test_api.py
```

* Sends multiple test requests to `/predict`
* Prints predictions and probabilities

---

## 7. Docker
#Use the link for the docker image access : docker image https://hub.docker.com/r/chettipellysrilatha/heart-mlops-api

### Build Docker Image

```bash
docker build -t heart-api .
```

### Run Container

```bash
docker run -p 8000:8000 heart-api
```

* API available at `http://127.0.0.1:8000`

---


## 8. CI/CD

A GitHub Actions workflow automates:

* Code linting & testing
* Docker image build
* Push Docker image to registry

Workflow location: `.github/workflows/ci.yml`

---
## 9. Logging
#MLflow UI
```bash
Default URL: http://127.0.0.1:5000
```
Use: View experiment runs, compare metrics, and download models.

#raining & Logging
---bash
python -m src.train
```
Loads preprocessed data
Trains models
Logs all parameters, metrics, and models to MLflow

# Model Evaluation

---bash
Script: src/evaluate.py
---
Functionality: Evaluate trained model(s) on test set and log metrics.

---bash
python -m src.evaluate
----
# To check the og requests, responses 
Timestamp, 
Model version, 
Input features,
Prediction result & probability,
Latency.

---bash
cat logs/predictions.log
---
  
Store logs in logs/ folder
* All API requests, responses, and latency are logged
* Logs saved to a file and SQLite database
* Includes model version for reproducibility

---

## 10. Summary

* Full ML workflow implemented: **Data → Model → API → Logging → Docker → CI/CD**
* Build a Heart Disease Detection system with a complete MLOps pipeline
* Data preparation and processing as the foundation for model training
* Training and evaluation of three algorithms: Logistic Regression, Random Forest, XGBoost
* Results presented through a user-friendly webpage
* Integration of MLflow for experiment tracking
* CI/CD pipeline implementation for automation and reliability
* Docker images produced for scalability and reproducibility
* Demonstrates importance of structured ML processes and collaboration
* Achievement: Full end-to-end pipeline delivered

# heart-mlops-capstone
