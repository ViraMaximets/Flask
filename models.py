from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from main import db
from sqlalchemy import create_engine



class Admin(db.Model):
    __tablename__ = 'admin'

    adminId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)


class Car(db.Model):
    __tablename__ = 'car'

    carId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    brand = db.Column(db.Integer, db.ForeignKey('brand.brandId'))
    tag = db.Column(db.Integer, db.ForeignKey('tag.tagId'))
    photoUrl = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False)


class Brand(db.Model):
    __tablename__ = 'brand'

    brandId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Rent(db.Model):
    __tablename__ = 'rent'

    rentId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    carId = db.Column(db.Integer, db.ForeignKey('car.carId'), nullable=False)
    #startT = db.Column(db.Date, nullable=False)
    #endT = db.Column(db.Date, nullable=False)
    startT = db.Column(db.String(10), nullable=False)
    endT = db.Column(db.String(10), nullable=False)
    status = db.Column(db.Integer, nullable=False)


class Tag(db.Model):
    __tablename__ = 'tag'

    tagId = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class User(db.Model):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)
