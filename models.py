from main import db, Base


class Admin(Base):
    __tablename__ = 'admin'

    adminId = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)

class Brand(Base):
    __tablename__ = 'brand'

    brandId = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    tagId = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Car(Base):
    __tablename__ = 'car'

    carId = db.Column(db.Integer, nullable=False, primary_key=True)

    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.brandId))
    brand = db.relationship(Brand, backref=db.backref('brand'))

    tag_id = db.Column(db.Integer, db.ForeignKey(Tag.tagId))
    tag = db.relationship(Tag, backref=db.backref('tag'))

    photoUrl = db.Column(db.String(200))
    status = db.Column(db.Integer, nullable=False)


class Rent(Base):
    __tablename__ = 'rent'

    rentId = db.Column(db.Integer, nullable=False, primary_key=True)

    car_id = db.Column(db.Integer, db.ForeignKey(Car.carId))
    car = db.relationship(Car, backref=db.backref('car'))

    #startT = db.Column(db.Date, nullable=False)
    #endT = db.Column(db.Date, nullable=False)
    startT = db.Column(db.String(20), nullable=False)
    endT = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    userId = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(40), nullable=False)
