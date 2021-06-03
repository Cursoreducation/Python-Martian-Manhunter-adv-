from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def kingdom_colors():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM kingdom_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index():
    return json.dumps({'kingdom_colors': kingdom_colors()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
