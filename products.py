from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Product, Inventory, Sale, SaleItem, User

# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create User
User1 = User(name="Admin", email="hayate58@gmail.com",
             picture='http://www.daviker.co.uk/wp-content/uploads/profile-blank.png')
session.add(User1)
session.commit()

"""
products = [
    {
        'sku': '754697343789',
        'name': 'Blue Lash',
        'URL': 'img/blue-lash-bluefront@2x.png',
        'cost': '23.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697344366',
        'name': 'Spark Lash',
        'URL': 'img/spark-lash-sparkfront@2x.png',
        'cost': '22.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697343857',
        'name': 'Brown Lash',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '23.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697344014',
        'name': 'Original Mink Fiber',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '20.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697344367',
        'name': 'Premade Fans',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '18.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697344367',
        'name': 'Two tone purple lash',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '23.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697343864',
        'name': 'Purple Lash',
        'URL': 'img/purple-lash-purplefront@2x.png',
        'cost': '23.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697344236',
        'name': 'Pheonix Lash',
        'URL': 'img/pheonix-phoenixlashfront 1@2x.png',
        'cost': '22.00',
        'category': 'Lashes'
    },
    {
        'sku': '754697343543',
        'name': 'Purple Glue',
        'URL': 'img/spark-lash-sparkfront@2x.png',
        'cost': '22.00',
        'category': 'Glue_Removers'
    },
    {
        'sku': '754697343932',
        'name': 'Red Glue',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '22.00',
        'category': 'Glue_Removers'
    },
    {
        'sku': '34123413241',
        'name': 'Silver Glue',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '22.00',
        'category': 'Glue_Removers'
    },
    {
        'sku': '754697343468',
        'name': 'Glue Remover Gel',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '22.00',
        'category': 'Glue_Removers'
    },
    {
        'sku': '754697343444',
        'name': 'Glue Remover Cream',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '22.00',
        'category': 'Glue_Removers'
    }, {
        'sku': '1',
        'name': 'J Tool',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '40.00',
        'category': 'Tweezers'
    },
    {
        'sku': '754697343529',
        'name': 'F Tool',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '40.00',
        'category': 'Tweezers'
    },
    {
        'sku': '754697343628',
        'name': 'M Tool',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '40.00',
        'category': 'Tweezers'
    },
    {
        'sku': '754697343505',
        'name': 'Vetus Tool',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '40.00',
        'category': 'Tweezers'
    }, {
        'sku': '1',
        'name': 'Lash Foam Cleanser',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '22.00', 'category': 'Cleaners'
    }, {
        'sku': '1',
        'name': 'Facial Wash Gel',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '25.00',
        'category': 'Cleaners'
    }, {
        'sku': '754697344366',
        'name': 'Eyelash Cleansing Cotton',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '10.00',
        'category': 'Cleaners'
    }, {
        'sku': '754697343680',
        'name': 'Eyelash & Lip Makeup Remover',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '10.00',
        'category': 'Cleaners'
    }, {
        'sku': '754697343697',
        'name': 'Flash Cleanser',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '10.00',
        'category': 'Cleaners'
    }, {
        'sku': '1',
        'name': 'Eye Gel Patch/100 pairs',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '110.00',
        'category': 'Other'
    }, {
        'sku': '754697344366',
        'name': 'Eye Gel Patch/1 single',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '1.50',
        'category': 'Other'
    }, {
        'sku': '754697344366',
        'name': 'Practice Lash',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '7.00',
        'category': 'Other'
    }, {
        'sku': '754697344366',
        'name': 'Microswab',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '7.00',
        'category': 'Other'
    }, {
        'sku': '7546973433451',
        'name': 'Mascara',
        'URL': 'img/brown-lash-brownfront@2x.png',
        'cost': '10.00',
        'category': 'Other'
    }, {
        'sku': '1',
        'name': 'Lash Extension Tape (30 tape set)',
        'URL': 'img/originalminkfiber-originalfront@2x.png',
        'cost': '35.00',
        'category': 'Other'
    }, {
        'sku': '754697344366',
        'name': 'Lash Tape (1 pair)',
        'URL': 'img/premade-fan-premadefans@2x.png',
        'cost': '2.00',
        'category': 'Other'
    }, {
        'sku': '754697343482',
        'name': 'Jade',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '5.00',
        'category': 'Other'
    }, {
        'sku': '754697343635',
        'name': 'Mannequin Head',
        'URL': 'img/two-tone-purple-lash-twotonepurplelashfront@2x.png',
        'cost': '25.00',
        'category': 'Other'
    }
]
"""

# Lashes
product1 = Product(sku='754697343789', name='Blue Lash',
                   URL='img/blue-lash-bluefront@2x.png', cost='23.00', category='Lashes')
inventory1 = Inventory(stockCount='100', product_id=product1.id)
session.add(product1)
session.add(inventory1)

product1 = Product(sku='754697344366', name='Spark Lash',
                   URL='img/spark-lash-sparkfront@2x.png', cost='22.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697343857', name='Brown Lash',
                   URL='img/brown-lash-brownfront@2x.png', cost='23.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697344014', name='Original Mink Fiber',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='20.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697344367', name='Premade Fans',
                   URL='img/premade-fan-premadefans@2x.png', cost='18.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697344367', name='Two tone purple lash',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='23.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697343864', name='Purple Lash',
                   URL='img/purple-lash-purplefront@2x.png', cost='23.00', category='Lashes')
session.add(product1)

product1 = Product(sku='754697344236', name='Pheonix Lash',
                   URL='img/pheonix-phoenixlashfront 1@2x.png', cost='22.00', category='Lashes')
session.add(product1)


# Glue and Removers
product1 = Product(sku='754697343543', name='Purple Glue',
                   URL='img/spark-lash-sparkfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product1)

product1 = Product(sku='754697343932', name='Red Glue',
                   URL='img/brown-lash-brownfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product1)

product1 = Product(sku='34123413241', name='Silver Glue',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product1)

product1 = Product(sku='754697343468', name='Glue Remover Gel',
                   URL='img/premade-fan-premadefans@2x.png', cost='22.00', category='Glue_Removers')
session.add(product1)

product1 = Product(sku='754697343444', name='Glue Remover Cream',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product1)


# Tweezers
product1 = Product(sku='1', name='J Tool',
                   URL='img/brown-lash-brownfront@2x.png', cost='40.00', category='Tweezers')
session.add(product1)

product1 = Product(sku='754697343529', name='F Tool',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='40.00', category='Tweezers')
session.add(product1)

product1 = Product(sku='754697343628', name='M Tool',
                   URL='img/premade-fan-premadefans@2x.png', cost='40.00', category='Tweezers')
session.add(product1)

product1 = Product(sku='754697343505', name='Vetus Tool',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='40.00', category='Tweezers')
session.add(product1)


# Cleaners
product1 = Product(sku='1', name='Lash Foam Cleanser',
                   URL='img/brown-lash-brownfront@2x.png', cost='22.00', category='Cleaners')
session.add(product1)

product1 = Product(sku='1', name='Facial Wash Gel',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='25.00', category='Cleaners')
session.add(product1)

product1 = Product(sku='754697344366', name='Eyelash Cleansing Cotton',
                   URL='img/premade-fan-premadefans@2x.png', cost='10.00', category='Cleaners')
session.add(product1)

product1 = Product(sku='754697343680', name='Eyelash & Lip Makeup Remover',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='10.00', category='Cleaners')
session.add(product1)

product1 = Product(sku='754697343697', name='Flash Cleanser',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='10.00', category='Cleaners')
session.add(product1)


# Others
product1 = Product(sku='1', name='Eye Gel Patch/100 pairs',
                   URL='img/brown-lash-brownfront@2x.png', cost='110.00', category='Other')
session.add(product1)

product1 = Product(sku='754697344366', name='Eye Gel Patch/1 single',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='1.50', category='Other')
session.add(product1)

product1 = Product(sku='754697344366', name='Practice Lash',
                   URL='img/premade-fan-premadefans@2x.png', cost='7.00', category='Other')
session.add(product1)

product1 = Product(sku='754697344366', name='Microswab',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='7.00', category='Other')
session.add(product1)

product1 = Product(sku='7546973433451', name='Mascara',
                   URL='img/brown-lash-brownfront@2x.png', cost='10.00', category='Other')
session.add(product1)

product1 = Product(sku='1', name='Lash Extension Tape (30 tape set)',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='35.00', category='Other')
session.add(product1)

product1 = Product(sku='754697344366', name='Lash Tape (1 pair)',
                   URL='img/premade-fan-premadefans@2x.png', cost='2.00', category='Other')
session.add(product1)

product1 = Product(sku='754697343482', name='Jade',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='5.00', category='Other')
session.add(product1)

product1 = Product(sku='754697343635', name='Mannequin Head',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='25.00', category='Other')
session.add(product1)

session.commit()

print "added products"
