from models import *
from datetime import date

user1 = User(username='Bob', email='bob@gmail.com', password='123')
brand1 = Brand(name='Audi')

car1 = Car(brand=brand1, model='A8', description="Best car you HAVE EVER SEEN!")
admin1 = Admin(username='Zoe', email='Zoe@gmail.com', password='987414')
rent1 = Rent(owner=user1, car=car1, startT=date.today(), endT=date.today())


db.session.add(user1)
db.session.add(brand1)
db.session.add(car1)
db.session.add(admin1)
db.session.add(rent1)

db.session.commit()
