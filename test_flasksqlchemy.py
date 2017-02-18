from flask import Flask, request, jsonify
from users import User
from ext import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/users', methods=['GET'])
def users():
    username = request.form.get('name')
    user = User(username)
    print('User id:%s' % user.id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
