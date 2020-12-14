from flask import jsonify, request
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.sql.elements import Null

from models import *
from schema import *


@app.route("/")
def index():
    return '<h1>    You are at home page <br/> ≧◠ᴥ◠≦</h1>'


@app.route('/cake')
def la():
    return '<h1>    cakes! <br/>🎂🎂🎂<br/>🎂🎂<br/>🎂 </h1>'


############################################# user ##############################################

@app.route("/user", methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = UserSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    user = User(username=result["username"], email=result["email"], password=result["password"])

    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/user", methods=['GET'])
def get_users():
    try:
        users = db.session.query(User).order_by(User.userId).all()
        user_schema = UserSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = user_schema.dump(users)
    except Exception:
        return jsonify({'response': "Cannot upload info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/user/<int:id>", methods=['GET'])
def get_user_by_id(id):
    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        result = db.session.query(User).filter(User.userId == id).order_by(User.userId).all()
        schema = UserSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = schema.dump(result)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/user/<int:id>", methods=['PUT'])
def update_user(id):

    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    result = request.get_json()
    if not result:
        return {"response": "No input data provided"}, 400

    try:
        if "username" in result:
            db.session.query(User).filter(User.userId == id).update(dict(username=result["username"]))
        if "email" in result:
            db.session.query(User).filter(User.userId == id).update(dict(email=result["email"]))
        if "password" in result:
            db.session.query(User).filter(User.userId == id).update(dict(password=result["password"]))
    except Exception:
        return jsonify({'response': "Updating failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)
############################################# admin ##############################################

@app.route("/admin", methods=['POST'])
def create_admin():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = AdminSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    admin = Admin(username=result["username"], email=result["email"], password=result["password"])

    try:
        db.session.add(admin)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/admin", methods=['GET'])
def get_admins():
    try:
        admins = db.session.query(Admin).order_by(Admin.adminId).all()
        admin_schema = AdminSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = admin_schema.dump(admins)
    except Exception:
        return jsonify({'response': "Cannot upload info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/admin/<int:id>", methods=['GET'])
def get_admin_by_id(id):

    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        result = db.session.query(Admin).filter(Admin.adminId == id).order_by(Admin.adminId).all()
        schema = AdminSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = schema.dump(result)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/admin/<int:id>", methods=['PUT'])
def update_admin(id):

    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    result = request.get_json()
    if not result:
        return {"response": "No input data provided"}, 400

    try:
        if "username" in result:
            db.session.query(Admin).filter(Admin.adminId == id).update(dict(username=result["username"]))
        if "email" in result:
            db.session.query(Admin).filter(Admin.adminId == id).update(dict(email=result["email"]))
        if "password" in result:
            db.session.query(Admin).filter(Admin.adminId == id).update(dict(password=result["password"]))
    except Exception:
        return jsonify({'response': "Updating failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


############################################# brand ##############################################

@app.route("/brand", methods=['POST'])
def create_brand():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = BrandSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    brand = Brand(name=result["name"])

    try:
        db.session.add(brand)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/brand", methods=['GET'])
def get_brands():
    try:
        brands = db.session.query(Brand).order_by(Brand.name).all()
        brand_schema = BrandSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = brand_schema.dump(brands)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


############################################# car ##############################################

@app.route("/car", methods=['POST'])
def create_car():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = CarSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    if db.session.query(Brand.brandId).filter_by(brandId=result["brand_id"]).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    car = Car(brand_id=result["brand_id"], model=result["model"], description=result["description"])

    try:
        db.session.add(car)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/car", methods=['GET'])
def get_cars():
    try:
        cars = db.session.query(Car).order_by(Car.carId).all()
        car_schema = CarSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = car_schema.dump(cars)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/car/<int:id>", methods=['GET'])
def get_car_by_id(id):
    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        result = db.session.query(Car).filter(Car.carId == id).order_by(Car.carId).all()
        schema = CarSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = schema.dump(result)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)
