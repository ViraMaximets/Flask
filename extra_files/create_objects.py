from models import *

admin1 = Admin(username='admin', email='admin@gmail.com',
            password=b'\\x05w\\xaf\\xa2a\\xd4\\xf8\\xc1\\xaeQ\\xd5\\xc1\\x98\\x92s\\xe9\\xbd%\\xb7r\\x95\\xe6\\x93#\\xed\\xd7gVkP\\x8a \\x91\\xdf-\\x11\\xf6\\xf2w\\x81I\\x1a\\xfb\\t\\xa3#\\xa9\\xe5+\\x9b0\\xf3\\x88p\\x0e\\x81\\x1d\\x99\\x98\\xbft\\xbdN\\xef')
brand1 = Brand(name='Audi')
brand2 = Brand(name='Tesla')
car1 = Car(brand=brand1, model='A8', description="Best car for you")
car2 = Car(brand=brand1, model='Q7', description="Fine")
car3 = Car(brand=brand2, model='xxx', description="")


db.session.add(admin1)
db.session.add(brand1)
db.session.add(car1)

db.session.add(brand2)
db.session.add(car2)
db.session.add(car3)

db.session.commit()
