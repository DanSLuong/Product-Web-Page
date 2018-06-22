import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    sku = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    URL = Column(String(250), nullable=False)
    cost = Column(Integer, nullable=False)
    reviews = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='product')


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'sku': self.sku,
            'name': self.name,
            'URL': self.URL,
            'cost': self.cost,
            'reviews': self.reviews,
            'id': self.id,
        }


engine = create_engine('sqlite:///products.db')

Base.metadata.create_all(engine)
