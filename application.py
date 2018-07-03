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
# Product, Inventory, Sale, SaleItem, Employee
from database_setup import Base, Blog, User
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
squareconnect.configuration.access_token = 'Key goes here'
# create an instance of the Catalog API class
api_instance = CatalogApi()


api_instances = []
api_instances2 = []
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
squaredata = []
while value < len(api_instances[0]):
    if api_instances[0][value].item_data:
        if api_instances[0][value].item_data.variations[0].item_variation_data.sku:
            cost = float(
                api_instances[0][value].item_data.variations[0].item_variation_data.price_money.amount)

            squaredata.append([api_instances[0][value].item_data.name,
                               api_instances[0][value].item_data.description,
                               api_instances[0][value].item_data.category_id,
                               api_instances[0][value].item_data.product_type,
                               api_instances[0][value].item_data.variations[0].id,
                               api_instances[0][value].item_data.variations[0].item_variation_data.item_id,
                               api_instances[0][value].item_data.image_url,
                               api_instances[0][value].item_data.variations[0].item_variation_data.sku,
                               cost/100,
                               api_instances[0][value].item_data.variations[0].item_variation_data.inventory_alert_type])
    value += 1
"""
for i in range(len(squaredata)):
      #for j in range(len(squaredata[i])):
      #      print (squaredata[i][j])
      print (squaredata[i][0], '|', squaredata[i][7])    
      print ('')
      """


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
    products = []
    for i in range(len(squaredata)):
        products.append(squaredata[i][0])
    return render_template('test2.html', products=products)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
