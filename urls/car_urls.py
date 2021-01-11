import jwt
from flask import jsonify, request

import urls.basic_urls as bu
from models import Car, Brand, app, db
from schema import CarSchema


@app.route("/car", methods=['POST'])
def create_car():
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

    data = request.get_json()
    if not data:
        return jsonify({"response": "No input data provided"}), 400

    try:
        result = CarSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 403

    if db.session.query(Brand.brandId).filter_by(brandId=result["brand_id"]).scalar() is None:
        return jsonify({'response': "Invalid brand_id found"}), 403

    car = Car(brand_id=result["brand_id"], model=result["model"], description=result["description"])

    db.session.add(car)
    db.session.commit()

    return jsonify({'response': "Success"}), 201


@app.route("/car", methods=['GET'])
def get_cars():
    cars = db.session.query(Car).order_by(Car.carId).all()
    car_schema = CarSchema(many=True)
    dump_data = car_schema.dump(cars)

    return jsonify({'response': dump_data}), 200


@app.route("/car/<int:id>/", methods=['GET'])
def get_car_by_id(id):
    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = db.session.query(Car).filter(Car.carId == id).order_by(Car.carId).all()
    schema = CarSchema(many=True)
    dump_data = schema.dump(result)

    return jsonify({'response': dump_data}), 200


@app.route("/car/<int:id>/", methods=['PUT'])
def update_car(id):
    auth_token = request.args.get('access_token')
    try:
        keys = bu.decode_auth_token(auth_token)
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Signature expired. Please log in again.'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token. Please log in again.'}), 401
    admin = keys[0]

    if admin == 0:
        return jsonify({'response': "This is not an admin"}), 403

    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}), 406

    result = request.get_json()
    if not result:
        return {"response": "No input data provided"}, 400

    if "description" in result:
        db.session.query(Car).filter(Car.carId == id).update(dict(description=str(result["description"])))
        db.session.commit()
    return jsonify({'response': "Success"}), 200


@app.route("/car/<int:id>/", methods=['DELETE'])
def delete_car(id):
    token = request.args.get('access_token')
    decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not admin"}), 403

    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid carId found"}), 406

    db.session.query(Car).filter(Car.carId == id).delete()
    db.session.commit()
    return jsonify({'response': "Success"}), 200
