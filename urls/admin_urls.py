import hashlib
import os

import jwt
import sqlalchemy
from sqlalchemy import exc
from flask import jsonify, request

import urls.basic_urls as bu
from models import Admin, app, db
from schema import AdminSchema


@app.route("/admin", methods=['POST'])
def create_admin():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = AdminSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 400

    if db.session.query(Admin.adminId).filter_by(username=result["username"]).scalar() is not None:
        return jsonify({'response': "Username is already used"}), 409

    password = result["password"]
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)
    storage = salt + key

    admin = Admin(username=result["username"], email=result["email"], password=storage)

    db.session.add(admin)
    db.session.commit()

    adminId = db.session.query(Admin.adminId).filter_by(username=result["username"]).scalar()

    encoded_jwt = bu.encode_auth_token(adminId, 1)
    return jsonify({'response': "Sign up successfully! Please LOG IN to get access token"}), 201


@app.route("/admin", methods=['GET'])
def get_admins():
    admins = db.session.query(Admin).order_by(Admin.adminId).all()
    admin_schema = AdminSchema(many=True)

    dump_data = admin_schema.dump(admins)
    for i in range(len(dump_data)):
        dump_data[i]['password'] = str(dump_data[i]['password'])

    return jsonify({'response': dump_data}), 200


@app.route("/admin/<int:id>", methods=['GET'])
def get_admin_by_id(id):
    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = db.session.query(Admin).filter(Admin.adminId == id).order_by(Admin.adminId).all()
    schema = AdminSchema(many=True)
    dump_data = schema.dump(result)
    dump_data[0]['password'] = str(dump_data[0]['password'])

    return jsonify({'response': dump_data}), 200


@app.route("/admin", methods=['PUT'])
def update_admin():
    auth_token = request.args.get('access_token')
    try:
        keys = bu.decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401

    admin = keys[0]
    id = keys[1]

    if admin == 0:
        return jsonify({'response': "This is not an admin"}), 403

    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = request.get_json()
    if not result:
        return jsonify({"response": "No input data provided"}), 400

    if "username" in result:
        db.session.query(Admin).filter(Admin.adminId == id).update(dict(username=result["username"]))
    if "email" in result:
        db.session.query(Admin).filter(Admin.adminId == id).update(dict(email=result["email"]))
    db.session.commit()

    return jsonify({'response': "Success"}), 200


@app.route("/admin", methods=['DELETE'])
def delete_admin():
    auth_token = request.args.get('access_token')
    try:
        keys = bu.decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401
    admin = keys[0]
    id = keys[1]

    if admin == 0:
        return jsonify({'response': "This is not an admin"}), 403

    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    db.session.query(Admin).filter(Admin.adminId == id).delete()
    db.session.commit()

    return jsonify({'response': "Success"}), 200
