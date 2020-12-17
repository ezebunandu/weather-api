import os
from typing import Optional
import dotenv
import httpx
from infrastructure import weather_cache

dotenv.load_dotenv()
api_key = os.getenv('OPEN_WEATHER_KEY')


async def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:

    if forecast := weather_cache.get_weather(city, state, country, units):
        return forecast

    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data["main"]

    weather_cache.set_weather(city, state, country, units, forecast)
    return forecast