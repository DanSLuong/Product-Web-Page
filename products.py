from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Product, Inventory, Sale, SaleItem, Employee, User

# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create User
User1 = User(name="Admin", email="lighteyesusa@gmail.com",
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
product = Product(sku='754697343789', name='Blue Lash',
                   URL='img/blue-lash-bluefront@2x.png', cost='23.00', category='Lashes')
inventory1 = Inventory(stockCount='100', product_id=product.id)
session.add(product)
session.add(inventory1)

product = Product(sku='754697344366', name='Spark Lash',
                   URL='img/spark-lash-sparkfront@2x.png', cost='22.00', category='Lashes')
session.add(product)

product = Product(sku='754697343857', name='Brown Lash',
                   URL='img/brown-lash-brownfront@2x.png', cost='23.00', category='Lashes')
session.add(product)

product = Product(sku='754697344014', name='Original Mink Fiber',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='20.00', category='Lashes')
session.add(product)

product = Product(sku='754697344367', name='Premade Fans',
                   URL='img/premade-fan-premadefans@2x.png', cost='18.00', category='Lashes')
session.add(product)

product = Product(sku='754697344367', name='Two tone purple lash',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='23.00', category='Lashes')
session.add(product)

product = Product(sku='754697343864', name='Purple Lash',
                   URL='img/purple-lash-purplefront@2x.png', cost='23.00', category='Lashes')
session.add(product)

product = Product(sku='754697344236', name='Pheonix Lash',
                   URL='img/pheonix-phoenixlashfront 1@2x.png', cost='22.00', category='Lashes')
session.add(product)


# Glue and Removers
product = Product(sku='754697343543', name='Purple Glue',
                   URL='img/spark-lash-sparkfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product)

product = Product(sku='754697343932', name='Red Glue',
                   URL='img/brown-lash-brownfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product)

product = Product(sku='34123413241', name='Silver Glue',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product)

product = Product(sku='754697343468', name='Glue Remover Gel',
                   URL='img/premade-fan-premadefans@2x.png', cost='22.00', category='Glue_Removers')
session.add(product)

product = Product(sku='754697343444', name='Glue Remover Cream',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='22.00', category='Glue_Removers')
session.add(product)


# Tweezers
product = Product(sku='1', name='J Tool',
                   URL='img/brown-lash-brownfront@2x.png', cost='40.00', category='Tweezers')
session.add(product)

product = Product(sku='754697343529', name='F Tool',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='40.00', category='Tweezers')
session.add(product)

product = Product(sku='754697343628', name='M Tool',
                   URL='img/premade-fan-premadefans@2x.png', cost='40.00', category='Tweezers')
session.add(product)

product = Product(sku='754697343505', name='Vetus Tool',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='40.00', category='Tweezers')
session.add(product)


# Cleaners
product = Product(sku='1', name='Lash Foam Cleanser',
                   URL='img/brown-lash-brownfront@2x.png', cost='22.00', category='Cleaners')
session.add(product)

product = Product(sku='1', name='Facial Wash Gel',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='25.00', category='Cleaners')
session.add(product)

product = Product(sku='754697344366', name='Eyelash Cleansing Cotton',
                   URL='img/premade-fan-premadefans@2x.png', cost='10.00', category='Cleaners')
session.add(product)

product = Product(sku='754697343680', name='Eyelash & Lip Makeup Remover',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='10.00', category='Cleaners')
session.add(product)

product = Product(sku='754697343697', name='Flash Cleanser',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='10.00', category='Cleaners')
session.add(product)


# Others
product = Product(sku='1', name='Eye Gel Patch/100 pairs',
                   URL='img/brown-lash-brownfront@2x.png', cost='110.00', category='Other')
session.add(product)

product = Product(sku='754697344366', name='Eye Gel Patch/1 single',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='1.50', category='Other')
session.add(product)

product = Product(sku='754697344366', name='Practice Lash',
                   URL='img/premade-fan-premadefans@2x.png', cost='7.00', category='Other')
session.add(product)

product = Product(sku='754697344366', name='Microswab',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='7.00', category='Other')
session.add(product)

product = Product(sku='7546973433451', name='Mascara',
                   URL='img/brown-lash-brownfront@2x.png', cost='10.00', category='Other')
session.add(product)

product = Product(sku='1', name='Lash Extension Tape (30 tape set)',
                   URL='img/originalminkfiber-originalfront@2x.png', cost='35.00', category='Other')
session.add(product)

product = Product(sku='754697344366', name='Lash Tape (1 pair)',
                   URL='img/premade-fan-premadefans@2x.png', cost='2.00', category='Other')
session.add(product)

product = Product(sku='754697343482', name='Jade',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='5.00', category='Other')
session.add(product)

product = Product(sku='754697343635', name='Mannequin Head',
                   URL='img/two-tone-purple-lash-twotonepurplelashfront@2x.png', cost='25.00', category='Other')
session.add(product)




employee = Employee(name='Sherin lee', description='Sherin lee is not only a professional lash artist, a business owner of two companies, but she is a lash extension educator/trainer, who trained over hundreds of students within the last two years.', extra='Check out our students success stories on our Course Training Page.', picture='team-mobile-sherinportrait@2x.png')
session.add(employee)

employee = Employee(name='Lina', description='Hi lash lovers ! My name is Lina and I love love love lashing ! I’ve been doing it for over a year now and couldn’t be happier with the career I have chosen for myself ! I’ve had my cosmetology license for over 5 years now and never really did anything with it. I know I love beauty, making people feel beautiful is what I was always passionate about. I love seeing my clients reactions once they wake up from their “lash naps” with gorgeous lashes! And the excitement on there faces is priceless! Creating beauty is what I truly love! ', picture='team-mobile-linaportrait@2x.png')
session.add(employee)

employee = Employee(name='Cynthia', description='Cynthia has been in beauty industry since 2015, following the top beauty trends all around the world. She is working as a graphic designer for over 6 years with not just design and production, but also digital marketing as well. Helping small businesses with logo design, website and posters. She has over 3 years of experience with customer service and doing consulting with small business owners. After learning eyelash extension skills, she was able to connect the techniques, products and graphic design, representing the designs better in social marketing.', extra='Now offering consultation.', picture='team-mobile-cynthiaportrait@2x.png')
session.add(employee)

employee = Employee(name='Christine', description='Christine is the Sales Manager of Light Eyes USA. Her background in sales began in 2011, with experience in beauty skin care for approximately two years. She oversees the L.A. branch of the company. After a meeting with Sherin at the IECSC beauty show at the Light Eyes USA booth, Sherin invited her to join the team to help build the brand together. She assists during the eyelash extension courses for the Southern California market.', picture='team-mobile-christineportrait@2x.png')
session.add(employee)

employee = Employee(name='Barry Ho', description='Barry Ho is a Chinese business product & skill advisor for the asia market with Barry’s experitise, in the lashing industry, assisted our founder in making Light Eyes USA possible. Barry, had many years experience in the lash industry, he taught over thousands of students in asia. Barry also owns the largest lash distributer company in Taichung, Taiwan. His expertise and experience includes, EYE VIS International Lash Artist Instructor / Director, Jeda Jovisa Eyelash Designers Association Trainer / Instructor, 2014 granted Korea International Eyelash Artist professional, part of the lash education board judge group, and appeared in Singapore as lash instructor for Apnetti.', picture='team-mobile-barryportrait@2x.png')
session.add(employee)


session.commit()

print "added products and employees"
