from tests.conftest import client
from config import Config

#
# def test_homepage(client):
#     response = client.get("/")
#     assert response.status_code == 200
#
#
# def test_search_weather(client):
#     Config.WEATHER_API_KEY = "50569510c1msh6d39f712d3097bap19cf4bjsn4a3857cc9fd4"
#     Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
#     Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
#     response = client.post("/search", data={"city": "london"})
#     assert response.status_code == 200
#     print(response.data)
#     assert b"Weather for London" in response.data