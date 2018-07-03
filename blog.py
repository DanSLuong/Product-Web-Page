from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Product, Inventory, Sale, SaleItem, Employee, Blog, User

# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Blog Posts
blog = Blog(title='Las Vegas IECSC 2018', date='Jun 30, 2018', pictureURL='img/blog-desktop-vegas-booth.png', story='Thank you for those who visited us at the Las Vegas IECSC Convention. It was nice meeting all local beauty professionals. We look forward to more conventions next year.')
session.add(blog)

blog = Blog(title='Las Vegas IECSC 2018', date='Jun 21, 2018', pictureURL='img/blog-desktop-vegas.png', story='Mark on your calendar if you will be at the Las Vegas IECSC. We will be at booth 1679. We will be teaching and doing live demo for volume lash. Come by to learn or get lashes from the most popular lash business owners in North California. We are able to duplicate our skills to students and staff with tips and marketing skills. Bring a notebook if needed, no video recording allowed. Instructor Jaye from Lash Allure and Sherin from Face-N-Body decided to work together to bring better skills to the lash community. Thank you all')
session.add(blog)

blog = Blog(title='Lash Extension', date='Nov 16, 2017', pictureURL='img/blog-desktop-lashessential.png', story='How lash extensions is essential to every woman!')
session.add(blog)

session.commit()

print "added products and employees"
