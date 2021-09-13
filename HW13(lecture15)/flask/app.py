# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()

app = Flask(__name__)

#app.config.from_object("config.Config")

api = Api(app)

#db.init_app(app)

with app.app_context():
    import routes.todo
    import routes.weather
    import routes.blog

    #db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')