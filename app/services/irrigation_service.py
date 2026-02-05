def calculate_irrigation(data: dict):
    """
    Rule-based irrigation logic.
    Expected input keys:
    - soil_moisture (0–100)
    - temperature (°C)
    - humidity (%)
    """

    soil_moisture = data.get("soil_moisture", 0)
    temperature = data.get("temperature", 25)
    humidity = data.get("humidity", 50)

    # Rule 1: Very dry soil
    if soil_moisture < 30:
        return {
            "irrigation": "ON",
            "reason": "Soil moisture is low"
        }

    # Rule 2: Hot and dry weather
    if temperature > 32 and humidity < 40:
        return {
            "irrigation": "ON",
            "reason": "High temperature and low humidity"
        }

    # Rule 3: Enough moisture
    return {
        "irrigation": "OFF",
        "reason": "Soil moisture is sufficient"
    }

