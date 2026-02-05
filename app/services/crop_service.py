from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "ml" / "crop_model.pkl"
ENCODER_PATH = BASE_DIR / "ml" / "soil_encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def recommend_crop(data: dict):
    features = [[
        data.get("temperature"),
        data.get("humidity"),
        data.get("ph"),
        data.get("rainfall"),
    ]]

    prediction = model.predict(features)
    return {"recommended_crop": prediction[0]}

