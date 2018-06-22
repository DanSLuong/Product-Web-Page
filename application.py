from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from functools import wraps

app = Flask(__name__)
APPLICATION_NAME = "Website for a client"


# Homepage
@app.route('/')
@app.route('/home/')
def showHome():
    return render_template('homemobile.html')

# Aboutus page
@app.route('/aboutus')
def showAboutUs():
    return render_template('aboutusmobile.html')

# Contact page
@app.route('/contact')
def showContact():
    return render_template('contactmobile.html')

# Products page
@app.route('/product/products')
def showProducts():
    return render_template('productmobile.html')

# Courses page
@app.route('/course_training/course')
def showCourse():
    return render_template('coursemobile.html')

@app.route('/blog')
def showBlog():
    return render_template('blogmobile.html')

@app.route('/product/shipping')
def showShipping():
    return render_template('shippingmobile.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)