from flask import Flask, render_template, request, jsonify, Response
import requests
from app import app
from config import Config


@app.route('/weather', methods=['GET'])
def weather():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather = data['list'][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)