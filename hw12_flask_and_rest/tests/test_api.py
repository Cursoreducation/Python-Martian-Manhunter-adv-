from config import Config
from tests.conftest import client, todos
import json


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_list(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_update(client):
    update_data = {
        "text": "blablabla"
    }

    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json['1'] == "blablabla"


def test_delete(client):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    response = client.get("/todos/1")
    assert response.status_code == 404


def test_search_weather(client):
    Config.WEATHER_API_KEY = "53493f042amsh58b54fe3ed83e24p195f98jsnf109acbc59d2"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.get('/weather?city=Lviv')
    assert response.status_code == 200
    response = client.get('/weather?city=Paris,Barcelona')
    assert response.status_code == 200
    response = client.get('/weather?city=B')
    assert response.status_code == 404
    response = client.get('/weather?city=.')
    assert response.status_code == 404
