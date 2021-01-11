import jwt
from flask import jsonify, request

import urls.basic_urls as bu
from models import Car, app, db, Rent, User
from schema import RentSchema


@app.route("/rent", methods=['POST'])
def create_rent():
    auth_token = request.args.get('access_token')
    try:
        keys = bu.decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401
    admin = keys[0]
    id = keys[1]

    if admin == 1:
        return jsonify({'response': "You are not a user"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"response": "No input data provided"}), 400

    try:
        result = RentSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 403

    if db.session.query(Car.carId).filter_by(carId=result["car_id"]).scalar() is None:
        return jsonify({'response': "Invalid car ID found"}), 404

    rent = Rent(owner_id=id, car_id=result["car_id"], startT=result["startTime"],
                endT=result["endTime"])
    db.session.add(rent)
    db.session.commit()

    return jsonify({'response': "Success"}), 201


@app.route("/rent", methods=['GET'])
def get_rents():
    auth_token = request.args.get('access_token')
    try:
        keys = bu.decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401
    admin = keys[0]
    id = keys[1]

    if admin == 1:
        return jsonify({'response': "You are not a user"}), 403

    result = db.session.query(Rent).filter(Rent.owner_id == id).order_by(Rent.rentId).all()
    schema = RentSchema(many=True)
    dump_data = schema.dump(result)

    return jsonify({'response': dump_data}), 200


@app.route("/rent/<int:rentId>/", methods=['DELETE'])
def delete_rent(rentId):
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
        return jsonify({'response': "You are not a user"}), 403

    if db.session.query(Rent.rentId).filter_by(rentId=rentId, owner_id=id).scalar() is None:
        return jsonify({'response': "No your`s rents with this ID found"}), 404

    db.session.query(Rent).filter(Rent.rentId == rentId).delete()
    db.session.commit()

    return jsonify({'response': "Success"}), 200
