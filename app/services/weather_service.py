import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(lat: float, lon: float):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    res = requests.get(url, timeout=5)
    res.raise_for_status()
    data = res.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "rainfall": data.get("rain", {}).get("1h", 0),
        "clouds": data["clouds"]["all"],
        "wind_speed": data["wind"]["speed"]
    }
