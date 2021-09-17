from tests.conftest import client
from config import Config

#
# def test_homepage(client):
#     response = client.get('/')
#     assert response.status_code == 200
#
#
# def test_search_weather(client):
#     Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
#     Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
#     Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
#     response = client.post("/search", data={"city": "london"})
#     assert response.status_code == 200
#     print(response.data)
#     assert b"Weather for London" in response.data