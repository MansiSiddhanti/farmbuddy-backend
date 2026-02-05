def process_sensor_data(payload: dict):
    return {
        "soil_moisture": float(payload["soil_moisture"]),
        "soil_temperature": float(payload["soil_temperature"]),
        "soil_ph": float(payload.get("soil_ph", 6.5)),
        "nitrogen": float(payload.get("nitrogen", 50))
    }
