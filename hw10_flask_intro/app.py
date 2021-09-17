# flask_web/app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello ladies!'


@app.route('/calc/<int:x>/<int:y>/<string:operation>')
def calc(x, y, operation):
    if operation == 'dif':
        return render_template('calc.html', x=x, y=y, operation='-', result=x - y)
    elif operation == 'sum':
        return render_template('calc.html', x=x, y=y, operation='+', result=x + y)
    elif operation == 'div':
        if y == 0:
            return render_template('calc.html', y=y)
        else:
            return render_template('calc.html', x=x, y=y, operation='/', result=x / y)
    elif operation == 'mult':
        return render_template('calc.html', x=x, y=y, operation='*', result=x * y)
    else:
        return render_template('calc.html', operation="Null")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
