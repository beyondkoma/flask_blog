# coding=utf-8
from flask import Flask
from plugin.ext import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
