def generate_report():
    """
    Dummy report generator.
    Can be extended later with DB / analytics.
    """
    return {
        "status": "success",
        "report": {
            "total_farms": 12,
            "irrigation_events": 38,
            "water_saved_liters": 1200
        }
    }
