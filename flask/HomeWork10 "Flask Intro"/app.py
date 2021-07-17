from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/calc/<int:x>/<int:y>/<string:choice>')
def calc(x, y, choice):
    if choice == 'sum' or choice == '+':
        return render_template('calc.html', x=x, y=y, ch='+', result=x + y)
    elif choice == 'sub' or choice == '-':
        return render_template('calc.html', x=x, y=y,  ch='-', result=x - y)
    elif choice == 'div' or choice == '/':
        if y == 0:
            return 'You can not divide by zero'
        else:
            return render_template('calc.html', x=x, y=y, ch='/', result=x / y)
    elif choice == 'mul' or choice == '*':
        return render_template('calc.html', x=x, y=y, ch='*', result=x * y)
    else:
        return 'Warning! Please, choose an operation!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
