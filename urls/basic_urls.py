import datetime

from flask import jsonify, request
import hashlib
import jwt
import sqlalchemy
from sqlalchemy import exc
from models import User, Admin, app, db
from schema import LoginSchema


def verify_pass(pass_db, pass_usr):
    salt_from_db = pass_db[:32]  # 32 является длиной соли
    key_from_db = pass_db[32:]
    key = hashlib.pbkdf2_hmac('sha256', pass_usr.encode('utf-8'), salt_from_db, 10000)
    return key, key_from_db


def encode_auth_token(id, admin):
    keys = {
        'id': id,
        'admin': admin,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'iat': datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(keys, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    return encoded_jwt


def decode_auth_token(auth_token):
    keys = jwt.decode(auth_token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    ans = [keys['admin'], keys['id']]
    return ans


@app.route("/", methods=['GET'])
def home():
    return jsonify('You are at home page'), 200


@app.route("/login", methods=['PUT'])
def login():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = LoginSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 403


    admin = result["admin"]
    if admin == 0:
        if db.session.query(User.userId).filter_by(username=result["username"]).scalar() is None:
            return jsonify({'response': "No user found"}), 404

        userId = db.session.query(User.userId).filter_by(username=result["username"]).scalar()
        passw = db.session.query(User.password).filter_by(userId=userId).scalar()

        key, key_from_storage = verify_pass(passw, result['password'])
        if key != key_from_storage:
            return jsonify({'response': "Password incorrect."}), 403

        encoded_jwt = encode_auth_token(userId, 0)

    else:
        if db.session.query(Admin.adminId).filter_by(username=result["username"]).scalar() is None:
            return jsonify({'response': "No user found"}), 404

        adminId = db.session.query(Admin.adminId).filter_by(username=result["username"]).scalar()
        passw = db.session.query(Admin.password).filter_by(adminId=adminId).scalar()

        key, key_from_storage = verify_pass(passw, result['password'])
        if key != key_from_storage:
            return jsonify({'response': "Password incorrect."}), 403

        encoded_jwt = encode_auth_token(adminId, 1)
    return jsonify({'JWT token:': encoded_jwt}), 200


@app.route("/logout", methods=['PUT'])
def logout():
    auth_token = request.args.get('access_token')
    try:
        keys = decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'You are already logged out.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token.'}), 401

    return jsonify({'response': "Success"}), 200
