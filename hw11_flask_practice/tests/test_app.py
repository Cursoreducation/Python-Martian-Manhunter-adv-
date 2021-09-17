from tests.conftest import client
from config import Config


class Mock:
    def __init__(self, *args, **kwargs):
        self.status_code = 200
        self.json_data = {"message": "accurate", "cod": "200", "count": 1, "list": [
            {"id": 2988507, "name": "Paris", "coord": {"lat": 48.8534, "lon": 2.3488},
             "main": {"temp": 292.57, "feels_like": 292.29, "temp_min": 289.97, "temp_max": 293.6, "pressure": 1005, "humidity": 66}, "dt": 1628280554, "wind": {"speed": 0.45, "deg": 203},
             "sys": {"country": "FR"}, "rain": None, "snow": None, "clouds": {"all": 0},
             "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n"}]}]}

    def json(self):
        return self.json_data


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"city": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_mock_search_weather(client, mocker):
    mocker.patch('requests.request', side_effect=Mock)
    response = client.post('/search', data={'cities': 'paris'})
    print(response)
    assert response.status_code == 200
    print(response.data)
    assert b'Weather for Paris' in response.data
