FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source
COPY src ./src
COPY api ./api
COPY models ./models
COPY data ./data
COPY README.md .

# environment for MLflow (local dir)
ENV MLFLOW_TRACKING_URI=/app/mlruns

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]