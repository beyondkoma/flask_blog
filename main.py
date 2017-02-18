# coding=utf-8
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'Hello World!'


# @app.route('/item/1/')
# def item(id):
#     pass

# with app.test_request_context():
#     print url_for('item', id='1')
#     print url_for('item', id=2, next='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
