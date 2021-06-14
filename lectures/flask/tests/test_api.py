from tests.conftest import client, todos
import json
from config import Config


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


def test_weather(client):
    Config.WEATHER_API_KEY = "8fd89dd0famsh2e179986560c1c9p1dfcedjsnd32b7762c9bc"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.get("/weather?city=london")
    assert response.status_code == 200
    assert response.json[0][0]['name'] == 'London'
    response2 = client.get("/weather?city=london,kyiv")
    assert response2.status_code == 200
    assert response2.json[0][0]['name'] == 'London'
    assert response2.json[1][0]['name'] == 'Kyiv'
    response3 = client.get("/weather?city=L")
    assert response3.status_code == 404
