from models import *

user1 = User(username='Bob', email='bob@gmail.com', password='123')
my_brand = Brand(name='Audi')
my_tag = Tag(name='audi-car')
car1 = Car(brand=my_brand, tag=my_tag, status=1)
my_rent = Rent(car=car1, startT='2020-12-2', endT='2020-12-4', status=1)

db.create_all()

db.session.add(user1)
db.session.add(my_brand)
db.session.add(my_tag)
db.session.add(car1)
db.session.add(my_rent)

db.session.commit()



