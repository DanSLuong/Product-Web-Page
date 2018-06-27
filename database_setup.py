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
        """Return object data in easily serializeable format"""
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
        """Return object data in easily serializeable format"""
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
        """Return object data in easily serializeable format"""
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
        """Return object data in easily serializable format"""
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
        """Return object data in easily serializable format"""
        return{
            'id': self.id,
            'itemSold': self.itemSold,
            'quantity': self.quantity,
        }

# engine = create_engine('sqlite:///products.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.create_all(engine)
