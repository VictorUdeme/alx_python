"""
importing flask
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{n}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


