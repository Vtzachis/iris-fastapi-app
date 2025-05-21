from fastapi import FastAPI
from app import schemas
from app.model import model  

app = FastAPI()

species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/predict", response_model=schemas.PredictionResponse)
def predict(features: schemas.IrisFeatures):
    data = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]
    prediction = model.predict([data])[0]
    species_name = species_map.get(prediction, "unknown")
    return {"species": species_name}