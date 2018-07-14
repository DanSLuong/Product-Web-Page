import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import *

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    extra = Column(String(250), nullable=False)
    picture = Column(String(250))

    
    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'name': self.name,
            'description': self.description,
            'extra': self.extra,
            'picture': self.picture,
            'id': self.id,
        }

        
class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    dateValue = Column(String(250), nullable=False)
    pictureURL = Column(String(250), nullable=False)
    story = Column(String(750), nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='blog')


    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'id': self.id,
            'title': self.title,
            'dateValue': self.date,
            'pictureURL': self.pictureURL,
            'story': self.story,
        }


# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.create_all(engine)
