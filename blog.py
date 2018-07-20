from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Blog, User

# engine = create_engine('postgresql://catalog:password@localhost/catalog')
engine = create_engine('sqlite:///lighteyesusa.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create User
User1 = User(name="Admin", email="lighteyesusa@gmail.com",
             picture='http://www.daviker.co.uk/wp-content/uploads/profile-blank.png')
session.add(User1)
session.commit()

# Blog Posts
blog = Blog(user_id=1,
            title='Lash Extension',
            dateValue='Nov 16, 2017',
            pictureURL='/static/img/lashessentials.png',
            story='How lash extensions is essential to every woman!')
session.add(blog)

blog = Blog(user_id=1,
            title='Las Vegas IECSC 2018',
            dateValue='Jun 21, 2018',
            pictureURL='/static/img/vegas.png',
            story='Mark on your calendar if you will be at the Las Vegas IECSC. We will be at booth 1679. We will be teaching and doing live demo for volume lash. Come by to learn or get lashes from the most popular lash business owners in North California. We are able to duplicate our skills to students and staff with tips and marketing skills. Bring a notebook if needed, no video recording allowed. Instructor Jaye from Lash Allure and Sherin from Face-N-Body decided to work together to bring better skills to the lash community. Thank you all')
session.add(blog)

blog = Blog(user_id=1,
            title='Las Vegas IECSC 2018',
            dateValue='Jun 30, 2018',
            pictureURL='/static/img/vegas-booth.png',
            story='Thank you for those who visited us at the Las Vegas IECSC Convention. It was nice meeting all local beauty professionals. We look forward to more conventions next year.')
session.add(blog)
session.commit()

print "added blog posts"
