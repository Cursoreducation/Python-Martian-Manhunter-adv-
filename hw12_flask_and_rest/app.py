# flask_web/app.py
import json

from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


@app.route("/search", methods=["POST"])
def search_weather():
    city = request.form.get("city")
    querystring = {
        "q": city,
        "cnt": "1",
        "mode": "null",
        "lon": "0",
        "type": "link, accurate",
        "lat": "0",
        "units": "metric",
    }

    headers = {
        "x-rapidapi-key": Config.WEATHER_API_KEY,
        "x-rapidapi-host": Config.WEATHER_API_HOST,
    }

    response = requests.request(
        "GET", Config.WEATHER_API_URL, headers=headers, params=querystring
    )
    if response.status_code == 200:
        data = response.json()
        weather = data["list"][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)


api = Api(app)

todos = {}


class Todo(Resource):
    def get(self, todo_id):
        try:
            with open("data.json", "r") as data_file:
                all_data = json.load(data_file)
                for i in all_data:
                    if i == str(todo_id):
                        data = {todo_id: all_data[i]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get("text")
        data = {todo_id: todos[todo_id]}
        with open("data.json", "r") as data_file:
            all_data = json.load(data_file)
            for i in all_data:
                if i == str(todo_id):
                    all_data[i] = todos[todo_id]
        with open("data.json", "w") as data_file:
            json.dump(all_data, data_file)
        return data

    def delete(self, todo_id):
        del todos[todo_id]
        with open("data.json", "r") as data_file:
            all_data = json.load(data_file)
            for i in list(all_data):
                if i == str(todo_id):
                    del all_data[i]
        with open("data.json", "w") as data_file:
            json.dump(all_data, data_file)
        return Response(todos, status=204)


class TodoList(Resource):
    def get(self):
        with open("data.json", "r") as data_file:
            all_data = json.load(data_file)
        return all_data

    def post(self):
        todos[request.json.get("todo_id", None)] = request.json.get("text", "")
        with open("data.json", "w") as data_file:
            json.dump(todos, data_file)
        return todos


class Weather(Resource):
    def get(self):
        c_list = request.args.getlist("city")
        querystring = {"q": c_list}
        headers = {
            "x-rapidapi-key": Config.WEATHER_API_KEY,
            "x-rapidapi-host": Config.WEATHER_API_HOST,
        }
        response = requests.request(
            "GET", Config.WEATHER_API_URL, headers=headers, params=querystring
        )
        if response.status_code == 200:
            data = response.json()
            return data
        return Response(status=404)


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")
api.add_resource(Weather, "/weather")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
