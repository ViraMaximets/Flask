import hashlib
import os

import jwt
from flask import jsonify, request

import urls.basic_urls as bu
from models import User, app, db
from schema import UserSchema


@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"response": "No input data provided"}), 400

    try:
        result = UserSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 400

    if db.session.query(User.userId).filter_by(username=result["username"]).scalar() is not None:
        return jsonify({'response': "Username is already used"}), 409

    password = result["password"]
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)
    storage = salt + key

    user = User(username=result["username"], email=result["email"], password=storage)
    db.session.add(user)
    db.session.commit()

    userId = db.session.query(User.userId).filter_by(username=result["username"]).scalar()
    encoded_jwt = bu.encode_auth_token(userId, 0)
    return jsonify({'response': "Sign up successfully! Please LOG IN to get access token"}), 201


@app.route("/user", methods=['GET'])
def get_users():
    users = db.session.query(User).order_by(User.userId).all()
    user_schema = UserSchema(many=True)
    dump_data = user_schema.dump(users)
    for i in range(len(dump_data)):
        dump_data[i]['password'] = str(dump_data[i]['password'])

    return jsonify({'response': dump_data}), 200


@app.route("/user/<int:id>", methods=['GET'])
def get_user_by_id(id):
    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = db.session.query(User).filter(User.userId == id).order_by(User.userId).all()
    schema = UserSchema(many=True)
    dump_data = schema.dump(result)
    dump_data[0]['password'] = str(dump_data[0]['password'])

    return jsonify({'response': dump_data}), 200


@app.route("/user", methods=['PUT'])
def update_user():
    try:
        auth_token = request.args.get('access_token')
        keys = bu.decode_auth_token(auth_token)

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401

    admin = keys[0]
    id = keys[1]

    if admin == 1:
        return jsonify({'response': "This is not a user"}), 403

    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = request.get_json()
    if not result:
        return jsonify({"response": "No input data provided"}), 400

    if "username" in result:
        db.session.query(User).filter(User.userId == id).update(dict(username=result["username"]))
    if "email" in result:
        db.session.query(User).filter(User.userId == id).update(dict(email=result["email"]))
    db.session.commit()

    return jsonify({'response': "Success"}), 200


@app.route("/user", methods=['DELETE'])
def delete_user():
    try:
        auth_token = request.args.get('access_token')
        keys = bu.decode_auth_token(auth_token)

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401

    admin = keys[0]
    id = keys[1]

    if admin == 1:
        return jsonify({'response': "This is not a user"}), 403

    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    db.session.query(User).filter(User.userId == id).delete()
    db.session.commit()
    return jsonify({'response': "Success"}), 200
