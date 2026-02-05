import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

np.random.seed(42)

data_size = 2000

data = pd.DataFrame({
    "soil_moisture": np.random.uniform(10, 70, data_size),
    "soil_temp": np.random.uniform(15, 40, data_size),
    "air_temp": np.random.uniform(15, 45, data_size),
    "humidity": np.random.uniform(30, 90, data_size),
    "rainfall": np.random.uniform(0, 10, data_size),
    "clouds": np.random.uniform(0, 100, data_size),
    "wind_speed": np.random.uniform(0, 10, data_size)
})

# Label generation logic (scientifically reasonable)
data["irrigation_required"] = (
    (data["soil_moisture"] < 30) &
    (data["rainfall"] < 2) &
    (data["air_temp"] > 28)
).astype(int)

X = data.drop("irrigation_required", axis=1)
y = data["irrigation_required"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=8,
    random_state=42
)
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
print("Model Accuracy:", acc)

joblib.dump(model, "irrigation_ml_model.pkl")
print("✅ ML model saved!")
