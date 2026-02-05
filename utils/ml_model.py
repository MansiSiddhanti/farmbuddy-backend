import joblib
import numpy as np

model = joblib.load("irrigation_ml_model.pkl")

def predict_irrigation_ml(weather, sensor):

    features = np.array([[
        sensor["soil_moisture"],
        sensor["soil_temperature"],
        weather["temperature"],
        weather["humidity"],
        weather["rainfall"],
        weather["clouds"],
        weather["wind_speed"]
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][prediction]

    return {
        "irrigation_required": bool(prediction),
        "confidence": round(probability * 100, 2)
    }
