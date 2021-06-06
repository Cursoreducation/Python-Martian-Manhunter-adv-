# flask_web/app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def kek(variable):
    print(variable)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return 'Hey, we have Flask in a Docker container!'


@app.route('/hello')
def hello():
    q = request.args.get("q", '')
    return "Search " + q


@app.route('/userprofile/<string:username>')
def userprofile(username):
    return "Hello " + username


@app.route('/calc/<int:x>/<int:y>')
def calc(x, y):
    arr = [5, 3, 6, 7, 8]
    return render_template('calc.html', x=x, y=y, sum=x+y, arr=arr)


@app.route('/template')
def template():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')