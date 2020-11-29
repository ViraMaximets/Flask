from main import db


class Admin(db.Model):
    __tablename__ = 'admin'

    adminId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __init__(self, userId=None, username=None, email=None, password=None):
        self.userId = userId
        self.username = username
        self.email = email
        self.password = password


class Car(db.Model):
    __tablename__ = 'car'

    carId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    brand = db.Column(db.Integer, db.ForeignKey('brand.brandId'), nullable=False)
    tag = db.Column(db.Integer, db.ForeignKey('tag.tagId'), nullable=False)
    photoUrl = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, carId=None, brand=None, tag=None, photoUrl=None, status=None):
        self.carId = carId
        self.brand = brand
        self.tag = tag
        self.photoUrl = photoUrl
        self.status = status


class Brand(db.Model):
    __tablename__ = 'brand'

    brandId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    cars = db.relationship('Car')

    def __init__(self, brandId=None, name=None):
        self.brandId = brandId
        self.name = name


class Rent(db.Model):
    __tablename__ = 'rent'

    rentId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    carId = db.Column(db.Integer, db.ForeignKey('car.carId'), nullable=False)
    startT = db.Column(db.DateTime, nullable=False)
    endT = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    car = db.relationship('Car')

    def __init__(self, rentId=None, carId=None, startT=None, endT=None, status=None):
        self.rentId = rentId
        self.carId = carId
        self.startT = startT
        self.endT = endT
        self.status = status


class Tag(db.Model):
    __tablename__ = 'tag'

    tagId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    cars = db.relationship('Car')

    def __init__(self, tagId=None, name=None):
        self.tagId = tagId
        self.name = name


class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __init__(self, userId=None, username=None, email=None, password=None):
        self.userId = userId
        self.username = username
        self.email = email
        self.password = password
