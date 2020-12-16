from typing import Optional
import dotenv
import os
import requests

dotenv.load_dotenv()
API_KEY = os.getenv('OPEN_WEATHER_KEY')


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'
    api_key = API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"

    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    return data["main"]
