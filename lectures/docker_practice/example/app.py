from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return 'Hi there'


@app.route("/test")
def test():
    return 'I am here'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
