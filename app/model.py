import joblib

# Load trained iris model
model = joblib.load("app/iris_model.pkl")

def predict_iris(features: list) -> str:
    prediction = model.predict([features])
    return prediction[0]  # Return the predicted class