from models import *

z = 2

user1 = User(userId=z, username='Bob', email='bob@gmail.com', password='123')
brand1 = Brand(brandId=z, name='Audi')
tag1 = Tag(tagId=z, name='audi-car')
car1 = Car(carId=z, brand=brand1, tag=tag1, status=1)
admin1 = Admin(adminId=z, username='Zoe', email='Zoe@gmail.com', password='987414')

user2 = User(userId=z+1, username='Bobter', email='boeb@gmail.com', password='11223')

rent1 = Rent(rentId=z, owner=user1, car=car1, startT="12.10.2020", endT='14.12.2020', status=1)

rent2 = Rent(rentId=z+1, owner=user2, car=car1, startT="12.10.2020", endT='14.12.2020', status=1)


db.session.add(user1)
db.session.add(brand1)
db.session.add(tag1)
db.session.add(car1)
db.session.add(admin1)

db.session.add(user2)



db.session.add(rent1)
db.session.add(rent2)

db.session.commit()
