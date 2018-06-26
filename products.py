from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Product, Inventory, Sale, SaleItem, User

engine = create_engine('sqlite:///products.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create User
User1 = User(name="Admin", email="hayate58@gmail.com",
             picture='http://www.daviker.co.uk/wp-content/uploads/profile-blank.png')
session.add(User1)
session.commit()




product1=Product(user_id=1, sku='754697343789', name='Blue Lash', URL='img/blue-lash-bluefront@2x.png', cost='23.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697344366', name='Spark Lash', URL='img/spark-lash-sparkfront@2x.png', cost='22.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697343857', name='Brown Lash', URL='img/brown-lash-brownfront@2x.png', cost='23.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697344014', name='Original Mink Fiber', URL='img/originalminkfiber-originalfront@2x.png', cost='20.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697344367', name='Premade Fans', URL='img/premade-fan-premadefans@2x.png', cost='18.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697344367', name='Two tone purple lash', URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='23.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697343864', name='Purple Lash', URL='img/purple-lash-purplefront@2x.png', cost='23.00', stockCount = 100, category='Lashes')
session.add(product1)

product1=Product(user_id=1, sku='754697344236', name='Pheonix Lash', URL='img/pheonix-phoenixlashfront 1@2x.png', cost='22.00', stockCount = 100, category='Lashes')
session.add(product1)



print "added products"