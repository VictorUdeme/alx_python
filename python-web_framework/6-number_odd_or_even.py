"""
importing flask
"""

from flask import Flask, render_template

app = Flask(__name__)

# Route: /
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Route: /hbnb
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"

# Route: /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C " + text.replace("_", " ")

# Route: /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    return "Python " + text.replace("_", " ")

# Route: /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{n} is a number"

# Route: /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', number=n)

# Route: /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    if n % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
