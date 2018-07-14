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
from database_setup import Base, Blog, User
from flask import session as login_session
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


# Redirect to square product page
@app.route('/product/products')
def showProducts():
    return redirect('https://squareup.com/store/light-eyes-usa', code=302)


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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
