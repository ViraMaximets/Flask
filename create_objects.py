from models import *
from datetime import date

user1 = User(username='Bob1', email='bob@gmail.com',
             password="'b'\\x0f\\xed\\xd6\\xe59\\xfa\\xc4\\xea1\\x7f\\xafu\\x9a\\x86\\x99c n\\xa1\\xe6\\x95\\x18\\xfcs"
                      "\\\\\\x99G\\xa0\\xe8}\\xc3z\\x84\\t\\x9eM\\t5\\x82\\x94\\xee\\xbd\\x8dB\\x95\\xba\\xa4\\x89\\xc3"
                      "M\\x001T\\x13C0L1I\\x1f\\xb93\\xf9\\xde'")

brand1 = Brand(name='Audi')
car1 = Car(brand=brand1, model='A8', description="Best car you HAVE EVER SEEN!")
admin1 = Admin(username='Zoe1', email='Zoe@gmail.com', password='987414')
rent1 = Rent(owner=user1, car=car1, startT="2020-12-08", endT="2020-12-10")

db.session.add(user1)
db.session.add(brand1)
db.session.add(car1)
db.session.add(admin1)
db.session.add(rent1)

db.session.commit()
