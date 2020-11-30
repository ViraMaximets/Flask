from models import Session, Car, Brand, Rent, Tag, User

session = Session

user1 = User(1, 'Bob', 'bob@gmail.com', '123')
my_brand = Brand(1, 'Audi')
my_tag = Tag(1, 'audi-car')
car1 = Car(1, brand=my_brand.brandId, tag=my_tag.tagId, status=1)
my_rent = Rent(1, carId=car1.carId, startT='2020-12-2', endT='2020-12-4', status=1)

session.add(user1)
session.add(my_brand)
session.add(my_tag)
session.add(car1)
session.add(my_rent)

session.commit()



