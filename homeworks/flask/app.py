# flask_web/app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/calc/<int:x>/<int:y>/<string:operation>')
def calc(x, y, operation):
    if operation == 'sum' or operation == '+':
        return render_template('calc.html', x=x, y=y, ans=x + y, sign="+")
    elif operation == 'div' or operation == '-':
        return render_template('calc.html', x=x, y=y, ans=x - y, sign="-")
    elif operation == 'dif' or operation == '|':
        return render_template('calc.html', x=x, y=y, ans=x / y, sign="/")
    elif operation == 'mul' or operation == '*':
        return render_template('calc.html', x=x, y=y, ans=x * y, sign="*")
    else:
        return 'Fail - incorrect data'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
