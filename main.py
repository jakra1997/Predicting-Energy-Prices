from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Energy Price Prediction API")

# Load models (example: assumes models are named model_1.pkl, model_2.pkl, etc.)
model_dir = "saved_models"
models = {}

for fname in os.listdir(model_dir):
    if fname.endswith(".pkl"):
        name = fname.replace(".pkl", "")
        models[name] = joblib.load(os.path.join(model_dir, fname))

# Define request format
class PredictionRequest(BaseModel):
    model_name: str
    features: list  # List of feature values

@app.post("/predict")
def predict_price(req: PredictionRequest):
    if req.model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")

    model = models[req.model_name]
    input_array = np.array(req.features).reshape(1, -1)

    try:
        prediction = model.predict(input_array)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"prediction": prediction}
