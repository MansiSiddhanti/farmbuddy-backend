import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
# Your CSV should have columns:
# temperature, soil_type, humidity, rainfall, crop
df = pd.read_csv("../data/crop_data.csv")

# Encode soil type
soil_encoder = LabelEncoder()
df["soil_type"] = soil_encoder.fit_transform(df["soil_type"])

# Features and target
X = df[["temperature", "soil_type", "humidity", "rainfall"]]
y = df["crop"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "crop_model.pkl")
joblib.dump(soil_encoder, "soil_encoder.pkl")

print("✅ Model trained and saved successfully")
