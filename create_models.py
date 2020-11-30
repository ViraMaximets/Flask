from models import Car, Brand, Rent, Tag, User
from main import db

db.create_all()

user1 = User(1, 'Bob', 'bob@gmail.com', '123')
my_brand = Brand(1, 'Audi')
my_tag = Tag(1, 'audi-car')
car1 = Car(1, brand=my_brand.brandId, tag=my_tag.tagId, status=1)
my_rent = Rent(1, carId=car1.carId, startT='2020-12-2', endT='2020-12-4', status=1)


db.session.add(user1)
db.session.add(my_brand)
db.session.add(my_tag)
db.session.add(car1)
db.session.add(my_rent)

db.session.commit()



