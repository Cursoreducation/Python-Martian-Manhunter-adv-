# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():

        weather = []
        cities = request.form.get("cities")
        cities = cities.replace(" ", "")
        cities_list = cities.split(",")
        for city in cities_list:
            querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "", "type": "link, accurate", "lat": "",
                           "units": "metric"}

            headers = {
                'x-rapidapi-key': Config.WEATHER_API_KEY,
                'x-rapidapi-host': Config.WEATHER_API_HOST
            }

            response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
            if response.status_code == 200:
                data = response.json()
                # weather = data['list'][0]
                try:
                    weather.append(data['list'][0])
                except(IndexError, ):
                    return render_template("error.html")

            else:
                return Response(status=404)
        return render_template("weather.html", weather=weather)



@app.route('/search_position', methods=['POST'])
def search_weather_position():

        weather = []
        lon = request.form.get("lon")
        lat = request.form.get("lat")
        querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                       "units": "metric"}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }

        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        data = response.json()

        if response.status_code == 200:
            weather.append(data['list'][0])
            return render_template("weather.html", weather=weather)
        else:
            weather.append(data)
            return render_template("incorrect_info.html", weather=weather)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
