from models import *

z = 1

user1 = User(userId=z, username='Bob', email='bob@gmail.com', password='123')
brand1 = Brand(brandId=z, name='Audi')

car1 = Car(carId=z, brand=brand1, model='A8', description="Best car you HAVE EVER SEEN!")
admin1 = Admin(adminId=z, username='Zoe', email='Zoe@gmail.com', password='987414')
rent1 = Rent(rentId=z, owner=user1, car=car1, startT="12.10.2020", endT='14.12.2020')

user2 = User(userId=z+1, username='Bobter', email='boeb@gmail.com', password='11223')
rent2 = Rent(rentId=z+1, owner=user2, car=car1, startT="12.10.2020", endT='14.12.2020', status=2)


db.session.add(user1)
db.session.add(brand1)
db.session.add(car1)
db.session.add(admin1)
db.session.add(rent1)

db.session.add(user2)
db.session.add(rent2)

db.session.commit()
