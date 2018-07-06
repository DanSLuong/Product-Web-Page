from __future__ import print_function
from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Blog, User, Customer, Product, Inventory, Sale, SaleItem, Employee
from flask import session as login_session
import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.catalog_api import CatalogApi
from squareconnect.apis.locations_api import LocationsApi
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from functools import wraps


# setup authorization
squareconnect.configuration.access_token = 'Token Key'
# create an instance of the Catalog API class
api_instance = CatalogApi()


api_instances = []
try:
    # ListLocations
    # api_response = api_instance.list_locations()
    # print (api_response.locations)
    # api_instances.append(api_response.locations)
    # List catalog list
    api_response = api_instance.list_catalog()
    api_instances.append(api_response.objects)
    # print (api_instances[0][90])

except ApiException as e:
    print ('Exception when calling CatalogApi->list_catalog: %s\n' % e)


# Pull product values
value = 1
count = 0
products = {}
squaredata = {}
for value in range(len(api_instances[0])):
      if api_instances[0][value].item_data:
            if api_instances[0][value].item_data.variations[0].item_variation_data.sku:
                  cost = float(
                          api_instances[0][value].item_data.variations[0].item_variation_data.price_money.amount)
                  
                  squaredata = {'name': api_instances[0][value].item_data.name,
                                'description': api_instances[0][value].item_data.description,
                                'category_id': api_instances[0][value].item_data.category_id,
                                'product_type': api_instances[0][value].item_data.product_type,
                                'product_id': api_instances[0][value].item_data.variations[0].id,
                                'other_id': api_instances[0][value].item_data.variations[0].item_variation_data.item_id,
                                'image_url': api_instances[0][value].item_data.image_url,
                                'product_sku': api_instances[0][value].item_data.variations[0].item_variation_data.sku,
                                'cost': cost/100,
                                'stock_count_alert': api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type}
                  products[count] = squaredata
                  count+=1
      value+=1


app = Flask(__name__)
APPLICATION_NAME = "Website for a client"

# Connect to the Database and creates a session
engine = create_engine('sqlite:///products.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Homepage
@app.route('/')
@app.route('/home/')
def showHome():
    return render_template('home.html')

# Aboutus page


@app.route('/aboutus')
def showAboutUs():
    return render_template('aboutus.html')

# Contact page


@app.route('/contact')
def showContact():
    return render_template('contactipad.html')

# Product pages


@app.route('/product/products')
def showProducts():
    return render_template('product.html')


"""
@app.route('/product/products')
def showProducts():
    return render_template('products.html')

# Shows infromation about the selected player
@app.route('/product/products/<int:product_id>/productinfo/')
@app.route('/product/products/<int:product_id>/')
def showProductInfo(team_id, player_id):
    product = session.query(Product).filter_by(id=product_id).one()
    return render_template('product.html', product=product)
"""


@app.route('/product/shipping')
def showShipping():
    return render_template('shipping.html')

# Under the services tab.


@app.route('/services/services')
def showServices():
    return render_template('services.html')


@app.route('/services/team')
def showTeam():
    return render_template('team.html')


@app.route('/services/clientcare')
def showClientCare():
    return render_template('clientcare.html')

# Course pages


@app.route('/course_training/course')
def showCourse():
    return render_template('coursemobile.html')


@app.route('/course_training/success_stories')
def showSuccessStories():
    return render_template('successstoriesipad.html')


@app.route('/course_training/educational')
def showEducational():
    return render_template('screen1.html')

# Blog
@app.route('/blog')
def showBlog():
    blogs = session.query(Blog).all()
    return render_template('blogipad.html', blogs=blogs)


@app.route('/blog/new/', methods=['GET', 'POST'])
def newBlogPost():
    if request.method == 'POST':
        newBlogPost = Blog(title=request.form['title'],
                           dateValue=request.form['dateValue'],
                           pictureURL=request.form['pictureURL'],
                           story=request.form['story'])
        session.add(newBlogPost)
        session.commit()
        return redirect(url_for('showBlog'))
    else:
        return render_template('newblogpost.html')


@app.route('/blog/<int:blog_id>/edit/', methods=['GET', 'POST'])
def editBlogPost(blog_id):
    editBlogPost = session.query(Blog).filter_by(id=blog_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editBlogPost.title = request.form['title']
        if request.form['dateValue']:
            editBlogPost.dateValue = request.form['dateValue']
        if request.form['pictureURL']:
            editBlogPost.pictureURL = request.form['pictureURL']
        if request.form['story']:
            editBlogPost.pictureURL = request.form['story']
        session.add(editBlogPost)
        session.comment()
        return redirect(url_for('showBlog'))
    else:
        return render_template('editblogpost.html', blog=editBlogPost)


@app.route('/blog/<int:blog_id>/delete/', methods=['GET', 'POST'])
def deleteBlogPost(blog_id):
    blogPostToDelete = session.query(Blog).filter_by(id=blog_id).one()
    if request.method == 'POST':
        session.delete(blogPostToDelete)
        session.commit()
        return redirect(url_for('showBlog'))
    else:
        return render_template('deleteblogpost.html', blog=blogPostToDelete)


@app.route('/test')
def showTest():
    return render_template('test2.html', products=products)


product_id = products[0]['product_id']
@app.route('/products/<int:product_id>/product')
@app.route('/products/<int:product_id>/')
def showProductInfo(product_id):
    product=products[product_id]
    return render_template('productinfo.html', product=product)


# Customer Info Stuff
@app.route('/customerinfo/<int:customer_id>/')
def showCustomerInfo(customer_id):
    customer = session.query(Customer).filter_by(id=customer_id).one()
    return render_template('showcustomerinfo.hmtl', customer=customer)


@app.route('/customerinfo/new', methods=['GET', 'POST'])
def newCustomer():
    if request.method == 'POST':
        newCustomerInfo = Customer(first_name=request.form['first_name'],
                                    last_name=request.form['last_name'],
                                    customer_email=request.form['customer_email'],
                                    address_line_1=request.form['address_line_1'],
                                    address_line_2=request.form['address_line_2'],
                                    state=request.form['state'],
                                    city=request.form['city'],
                                    zip_code=request.form['zip_code']
                                    )
        session.add(newCustomerInfo)
        session.commit()
        return redirect(url_for('showCustomerInfo'))
    else:
        return render_template('newcustomer.hmtl')


@app.route('/customerinfo/<int:customer_id>/edit/', methods=['GET', 'POST'])
def editCustomer(customer_id):
    editCustomer = session.query(Customer).filter_by(id=customer_id).one()
    if request.method == 'POST':
        if request.form['first_name']:
            editCustomer.first_name = request.form['first_name']
        session.add(editCustomer)
        session.commit()
        return redirect(url_for('showCustomerInfo'))
    else:
        return render_template('editcustomer.html', customer=editCustomer)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
