#!/usr/bin/python3
"""
This will start the Flask application
"""

from flask import flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """This returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port-5000')
