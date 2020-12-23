from flask import jsonify, request
import hashlib
import os
import jwt
from functools import wraps

from models import *
from schema import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        # http://127.0.0.1:5000/route?token=alshfjfjdklsfj89549834ur

        if not token:
            return jsonify({'message': 'You are not authorised'}), 403

        try:
            jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route("/")
def index():
    return '<h1>    You are at home page 🎂 <br/> ≧◠ᴥ◠≦</h1>'


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

    x = db.session.query(User).filter(User.username == result["username"]).order_by(User.userId).all()
    if len(str(x)) > 2:
        return jsonify({'response': "Username is already used"}, 407)

    password = result["password"]
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)

    storage = salt + key
    storage1 = str(storage)

    user = User(username=result["username"], email=result["email"], password=storage1)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    us = db.session.query(User).filter(User.username == result["username"]).order_by(User.userId).all()
    us = str(us)
    userId = us[7:-2]
    encoded_jwt = jwt.encode({"id": userId, "pass": storage1, "admin": 0}, app.config['SECRET_KEY'],
                             app.config['JWT_ALGORITHM'])

    return jsonify({'Your unique JWT token:': encoded_jwt}, 200)

@app.route("/login", methods=['GET'])
def login():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = LoginSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)


    password = result["password"]
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)

    storage = salt + key
    storage1 = str(storage)

    admin = result["admin"]
    if admin == 0:
        try:
            a = db.session.query(User.username).filter_by(username=result["username"])
            print(a)
            if a is None:
                return jsonify({'response': "No username found"}, 404)
        except Exception:
            return jsonify({'response': "Cannot GET username"}, 404)

        try:
            b = db.session.query(User.password).filter_by(password=storage1)
            print("b",b)
            if b is None:
                return jsonify({'response': "No password found"}, 404)
        except Exception:
            return jsonify({'response': "Cannot GET info"}, 404)

        us = db.session.query(User).filter(User.username == result["username"]).order_by(User.userId).all()


    else:
        try:
            a = db.session.query(Admin.username).filter_by(username=result["username"])
            print(a)
            if a is None:
                return jsonify({'response': "No username found"}, 404)
        except Exception:
            return jsonify({'response': "Cannot GET username"}, 404)

        try:
            b = db.session.query(Admin.password).filter_by(password=storage1)
            print("b", b)
            if b is None:
                return jsonify({'response': "No password found"}, 404)
        except Exception:
            return jsonify({'response': "Cannot GET info"}, 404)

        us = db.session.query(Admin).filter(Admin.username == result["username"]).order_by(Admin.adminId).all()

    us = str(us)
    userId = us[7:-2]
    encoded_jwt = jwt.encode({"id": userId, "pass": storage1, "admin": 0}, app.config['SECRET_KEY'],
                             app.config['JWT_ALGORITHM'])

    return jsonify({'Your JWT token:': encoded_jwt}, 200)

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


@app.route("/user", methods=['PUT'])
@token_required
def update_user(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 1:
        return jsonify({'response': "This is not a user"}, 404)

    id = decoded['id']

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


@app.route("/user", methods=['DELETE'])
def delete_user(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 1:
        return jsonify({'response': "This is not a user"}, 404)

    id = decoded['id']

    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        db.session.query(User).filter(User.userId == id).delete()
    except Exception:
        return jsonify({'response': "Deleting failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


############################################# admin ############################################################################################

@app.route("/admin", methods=['POST'])
def create_admin():
    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = AdminSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    x = db.session.query(Admin).filter(Admin.username == result["username"]).order_by(Admin.adminId).all()
    if len(str(x)) > 2:
        return jsonify({'response': "Username is already used"}, 407)

    # hashing start
    password = result["password"]
    salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 10000)

    # Хранение как
    storage = salt + key
    storage1 = str(storage)
    # Получение значений обратно
    # salt_from_storage = storage1[:32]  # 32 является длиной соли
    # key_from_storage = storage1[32:]
    # hashing end

    admin = Admin(username=result["username"], email=result["email"], password=storage1)

    try:
        db.session.add(admin)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a call"}, 402)


    us = db.session.query(User).filter(User.username == result["username"]).order_by(User.userId).all()
    us = str(us)
    Id = us[7:-2]
    encoded_jwt = jwt.encode({"id": Id, "pass": storage1, "admin": 1}, app.config['SECRET_KEY'],
                             app.config['JWT_ALGORITHM'])

    return jsonify({'Your unique JWT token:': encoded_jwt}, 200)


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


@app.route("/admin", methods=['PUT'])
def update_admin(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "This is not an admin"}, 404)

    id = decoded['id']

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


@app.route("/admin", methods=['DELETE'])
def delete_admin(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "This is not an admin"}, 404)

    id = decoded['id']

    if db.session.query(Admin.adminId).filter_by(adminId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        db.session.query(Admin).filter(Admin.adminId == id).delete()
    except Exception:
        return jsonify({'response': "Deleting failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


############################################# brand ############################################################################################

@app.route("/brand", methods=['POST'])
@token_required
def create_brand(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not an admin"}, 404)

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
        brands = db.session.query(Brand).order_by(Brand.brandId).all()
        brand_schema = BrandSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = brand_schema.dump(brands)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/brand/<int:id>", methods=['DELETE'])
def delete_brand(id, *args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not an admin"}, 404)

    if db.session.query(Brand.brandId).filter_by(brandId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        db.session.query(Brand).filter(Brand.brandId == id).delete()
    except Exception:
        return jsonify({'response': "Deleting failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


############################################# car ############################################################################################

@app.route("/car", methods=['POST'])
@token_required
def create_car(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not an admin"}, 404)


    data = request.get_json()
    if not data:
        return jsonify({"response": "No input data provided"}, 400)

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


@app.route("/car/<int:id>/", methods=['GET'])
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


@app.route("/car/<int:id>/", methods=['PUT'])
@token_required
def update_car(id, *args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not an admin"}, 404)

    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    result = request.get_json()
    if not result:
        return {"response": "No input data provided"}, 400

    try:
        if "description" in result:
            db.session.query(Car).filter(Car.carId == id).update(dict(description=result["description"]))
    except Exception:
        return jsonify({'response': "Updating failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/car/<int:id>/", methods=['DELETE'])
@token_required
def delete_car(id, *args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 0:
        return jsonify({'response': "You are not admin"}, 404)

    if db.session.query(Car.carId).filter_by(carId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        db.session.query(Car).filter(Car.carId == id).delete()
    except Exception:
        return jsonify({'response': "Deleting failed"}, 403)

    try:
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


############################################# rent ############################################################################################

@app.route("/rent", methods=['POST'])
@token_required
def create_rent(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 1:
        return jsonify({'response': "You are not a user"}, 404)


    data = request.get_json()
    if not data:
        return {"response": "No input data provided"}, 400

    try:
        result = RentSchema().load(data)
    except Exception:
        return jsonify({'response': "Invalid input"}, 403)

    if db.session.query(Car.carId).filter_by(carId=result["car_id"]).scalar() is None:
        return jsonify({'response': "Invalid car ID found"}, 404)


    rent = Rent(owner_id=decoded['id'], car_id=result["car_id"], startT=result["startTime"],
                endT=result["endTime"])

    try:
        db.session.add(rent)
        db.session.commit()
    except Exception:
        return jsonify({'response': "Database refused a request"}, 402)

    return jsonify({'response': "Success"}, 200)


@app.route("/rent", methods=['GET'])
@token_required
def get_rents(*args):
    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 1:
        return jsonify({'response': "You are not a user"}, 404)

    id = decoded['id']

    if db.session.query(User.userId).filter_by(userId=id).scalar() is None:
        return jsonify({'response': "Invalid ID found"}, 404)

    try:
        result = db.session.query(Rent).filter(Rent.owner_id == id).order_by(Rent.rentId).all()
        schema = RentSchema(many=True)
    except Exception:
        return jsonify({'response': "Cannot GET info"}, 404)

    try:
        dump_data = schema.dump(result)
    except Exception:
        return jsonify({'response': "Cannot DISPLAY info"}, 405)

    return jsonify({'response': dump_data}, 200)


@app.route("/rent/<int:rentId>/", methods=['DELETE'])
@token_required
def delete_rent(rentId, *args):

    try:
        token = request.args.get('token')
        decoded = jwt.decode(token, app.config['SECRET_KEY'], app.config['JWT_ALGORITHM'])
    except Exception:
        return jsonify({'response': "Decode token failed"}, 403)

    if decoded['admin'] == 1:
        return jsonify({'response': "You are not a user"}, 404)

    if db.session.query(Rent.rentId).filter_by(rentId=rentId).scalar() is None:
        return jsonify({'response': "Invalid rent ID found"}, 404)

    if db.session.query(Rent).filter(Rent.owner_id == decoded['id']).scalar() is None:
        return jsonify({'response': "No rent with this rentId available"}, 405)

    try:
        db.session.query(Rent).filter(Rent.rentId == rentId).delete()
        db.session.commit()
    except Exception:
        return jsonify({'response': "Deleting failed"}, 402)


    return jsonify({'response': "Success"}, 200)

