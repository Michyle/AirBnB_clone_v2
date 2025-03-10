#!/usr/bin/python3
"""
This will start the flask application
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
	"""this will return Hello HBNB!"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""This will return HBNB"""
	return 'HBNB'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
