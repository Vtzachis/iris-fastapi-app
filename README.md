# 🌼 Iris Flower Classification API (FastAPI + ML)

This project is a simple REST API for predicting the species of an Iris flower based on its sepal and petal measurements. It uses a trained scikit-learn model and is built using the FastAPI framework.

## 🚀 Features

- FastAPI backend
- Pydantic data validation
- RESTful endpoint for ML predictions
- Trained model included (iris_model.pkl)

## 📦 Requirements

Install dependencies using:

bash
pip install -r requirements.txt


## ▶️ How to Run
bash
uvicorn app.main:app --reload

Then visit:
http://127.0.0.1:8000/docs to access the interactive Swagger UI.

## 📬 API Endpoint
Input JSON:
json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

## 📁 Project Structure
iris-fastapi-app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── iris_model.pkl
├── requirements.txt
└── README.md


