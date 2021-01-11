import jwt
from flask import jsonify, request

import urls.basic_urls as bu
from models import Brand, app, db
from schema import BrandSchema


@app.route("/brand", methods=['POST'])
def create_brand():
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
        return {"response": "No input data provided"}, 400

    try:
        result = BrandSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}), 403

    brand = Brand(name=result["name"])
    db.session.add(brand)
    db.session.commit()

    return jsonify({'response': "Success"}), 201


@app.route("/brand", methods=['GET'])
def get_brands():
    brands = db.session.query(Brand).order_by(Brand.brandId).all()
    brand_schema = BrandSchema(many=True)
    dump_data = brand_schema.dump(brands)

    return jsonify({'response': dump_data}), 200


@app.route("/brand/<int:id>", methods=['DELETE'])
def delete_brand(id):
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

    if db.session.query(Brand.brandId).filter_by(brandId=id).scalar() is None:
        return jsonify({'response': "Invalid brand ID found"}), 406

    db.session.query(Brand).filter(Brand.brandId == id).delete()
    db.session.commit()

    return jsonify({'response': "Success"}), 200
