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


class Customer(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    customer_email = Column(String(250), nullable=False)
    address_line_1 = Column(String(250), nullable=False)
    address_line_2 = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    zip_code = Column(String(250), nullable=False)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'customer_email': self.customer_email,
            'address_line_1': self.address_line_1,
            'address_line_2': self.address_line_2,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'id': self.id,
        }

        
class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    dateValue = Column(String(250), nullable=False)
    pictureURL = Column(String(250), nullable=False)
    story = Column(String(750), nullable=False)
    
    #user_id = Column(Integer, ForeignKey('user.id'))
    #user = relationship(User, backref='blog')


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


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    sku = Column(FLOAT, nullable=False)
    name = Column(String(250), nullable=False)
    URL = Column(String(250), nullable=False)
    cost = Column(NUMERIC(12,2), nullable=False)
    category = Column(String(250), nullable=False)

    
    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'sku': self.sku,
            'name': self.name,
            'URL': self.URL,
            'cost': self.cost,
            'reviews': self.reviews,
            'stockCount': self.stockCount,
            'category': self.category,
            'id': self.id,
        }


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    stockCount = Column(Integer, nullable=False)

    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship(Product, backref=backref('inventory', cascade='all, delete'))
    

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'stockCount': self.stockCount,
            'id': self.id,
        }


class ProductReviews(Base):
    __tablename__ = 'productReviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'rating': self.rating,
            'id': self.id,
        }


class Sale(Base):
    __tablename__ = 'sale'

    # SaleTransactionId
    id = Column(Integer, primary_key=True)
    # dateTime = Column(datetime(), nullable=False)
    totalSale = Column(Integer, nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='sale')


    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'id': self.id,
            'dateTime': self.dateTime,
            'totalSale': self.totalSale,
        }


class SaleItem(Base):
    __tablename__ = 'saleItem'

    id = Column(Integer, primary_key=True)
    itemSold = Column(String(250), nullable=False)
    quantity = Column(Integer, nullable=False)
    
    # SaleTransactionId
    sale_id = Column(Integer, ForeignKey('sale.id'))
    sale = relationship(Sale, backref=backref('saleItem', cascade='all, delete'))
    # ProductID
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship(Product, backref=backref('saleItem', cascade='all, delete'))
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref='saleItem')


    @property
    def serialize(self):
        # Return object data in easily serializable format
        return{
            'id': self.id,
            'itemSold': self.itemSold,
            'quantity': self.quantity,
        }



# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.create_all(engine)
