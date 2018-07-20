from flask import (Flask,
                    render_template,
                    request, redirect,
                    jsonify,
                    url_for,
                    flash,
                    g)
from flask_mail import Mail, Message
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Blog, User
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from functools import wraps
import os


app = Flask(__name__)

APPLICATION_NAME = "Light Eyes USA"
# CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
CLIENT_ID = json.loads(open('/var/www/FlaskApp/FlaskApp/client_secrets.json', 'r').read())['web']['client_id']

# Connect to the Database and creates a session
engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('EMAIL_USER'),
    "MAIL_PASSWORD": os.environ.get('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;' \
              'height: 300px;' \
              'border-radius: 150px;' \
              '-webkit-border-radius: 150px;' \
              '-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showBlog'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showBlog'))


# Require Login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('showLogin', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# Mail info
def sendMailCustomer(mail_recipients, email_body):
    with mail.app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[mail_recipients],
                      body=email_body)
        mail.send(msg)


def sendMailCompany(subject, mail_recipients, email_body):
    with mail.app.app_context():
        msg = Message(subject=subject,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[mail_recipients],
                      body=email_body)
        mail.send(msg)

# JSON Serialized result
@app.route('/blog/JSON')
def blogJSON():
    blogs = session.query(Blog).all()
    return jsonify(blogs=[i.serialize for i in blogs])



# Homepage
@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['GET', 'POST'])
def showHome():
    if request.method == 'POST':

        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)

        return redirect(url_for('showHome'))
    else:
        return render_template('home.html')


# Aboutus page
@app.route('/aboutus', methods=['GET', 'POST'])
@app.route('/aboutus/', methods=['GET', 'POST'])
def showAboutUs():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)

        return redirect(url_for('showAboutUs'))
    else:
        return render_template('aboutus.html')


# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def showContact():
    if request.method == 'POST':
        if request.form['customerEmail']:
            full_name=request.form['Full_Name']
            email=request.form['customerEmail']
            phone=request.form['Phone']
            message=request.form['Message']
            message_body="Customer Name: " + full_name + "  |  Customer Phone: " + phone + "  |  Message: " + message
            subject="Customer Inquery"
            email_body= "Thank you for contacting us. Our team will get back to you as soon as we can!"

            sendMailCustomer(email, email_body)
            sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), message_body)
            return render_template('successfulsubmit.html')
        elif request.form['ClientEmail']:
            subject="Email Subscribe Request"
            mail_recipients=request.form['ClientEmail']
            email_body= "Thank you for joining our mailing list!"

            sendMailCustomer(mail_recipients, email_body)
            sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)

            return render_template('successfulsubmit.html')
        else:
            return render_template('unsuccessfulsubmit.html')
    else:
        return render_template('contactipad.html')


# Redirect to square product page
@app.route('/product/products')
def showProducts():
    return redirect('https://squareup.com/store/light-eyes-usa', code=302)


@app.route('/product/shipping', methods=['GET', 'POST'])
def showShipping():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)

        return redirect(url_for('showShipping'))
    else:
        return render_template('shipping.html')


# Under the services tab.
@app.route('/services/services', methods=['GET', 'POST'])
def showServices():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showServices'))
    else:
        return render_template('services.html')


@app.route('/services/team', methods=['GET', 'POST'])
def showTeam():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showTeam'))
    else:
        return render_template('team.html')


@app.route('/services/clientcare', methods=['GET', 'POST'])
@app.route('/services/clientcare/', methods=['GET', 'POST'])
def showClientCare():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showClientCare'))
    else:
        return render_template('clientcare.html')

# Course pages
@app.route('/course_training/course', methods=['GET', 'POST'])
@app.route('/course_training/course/', methods=['GET', 'POST'])
def showCourse():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showCourse'))
    else:
        return render_template('coursemobile.html')


@app.route('/course_training/success_stories', methods=['GET', 'POST'])
@app.route('/course_training/success_stories/', methods=['GET', 'POST'])
def showSuccessStories():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showSuccessStories'))
    else:
        return render_template('successstoriesipad.html')


@app.route('/course_training/educational', methods=['GET', 'POST'])
@app.route('/course_training/educational/', methods=['GET', 'POST'])
def showEducational():
    if request.method == 'POST':
        subject="Email Subscribe Request"
        mail_recipients=request.form['ClientEmail']
        email_body= "Thank you for joining our mailing list!"

        sendMailCustomer(mail_recipients, email_body)
        sendMailCompany(subject, mail.app.config.get("MAIL_USERNAME"), mail_recipients)
        
        return redirect(url_for('showEducational'))
    else:
        return render_template('educational.html')


# Blog
@app.route('/blog')
def showBlog():
    blogs = session.query(Blog).order_by(Blog.id.desc()).all()
    # return render_template('test.html', blogs=blogs)
    return render_template('blogipad.html', blogs=blogs)
    # return render_template('home.html')


@app.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def newBlogPost():
    if login_session['email'] != 'lighteyesusa@gmail.com':
        return "<script>function myFunction()" \
               "{alert('You are not allowed access to this page!');}" \
               "</script><body onload='myFunction()'>"
    if request.method == 'POST':
        newBlogPost = Blog(title=request.form['title'],
                           dateValue=request.form['dateValue'],
                           pictureURL="img/" + request.form['pictureURL'],
                           story=request.form['story'])
        session.add(newBlogPost)
        session.commit()
        return redirect(url_for('showBlog'))
    else:
        return render_template('newblogpost.html')


@app.route('/blog/<int:blog_id>/edit/', methods=['GET', 'POST'])
@login_required
def editBlogPost(blog_id):
    editBlogPost = session.query(Blog).filter_by(id=blog_id).one()
    if login_session['email'] != 'lighteyesusa@gmail.com':
        return "<script>function myFunction()" \
               "{alert('You are not allowed access to this page!');}" \
               "</script><body onload='myFunction()'>"
    if request.method == 'POST':
        if request.form['title']:
            editBlogPost.title = request.form['title']
        if request.form['dateValue']:
            editBlogPost.dateValue = request.form['dateValue']
        if request.form['pictureURL']:
            editBlogPost.pictureURL = request.form['pictureURL']
        if request.form['story']:
            editBlogPost.story = request.form['story']
        session.add(editBlogPost)
        session.comment()
        return redirect(url_for('showBlog'))
    else:
        return render_template('editblogpost.html', blog=editBlogPost)


@app.route('/blog/<int:blog_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteBlogPost(blog_id):
    blogPostToDelete = session.query(Blog).filter_by(id=blog_id).one()
    if login_session['email'] != 'lighteyesusa@gmail.com':
        return "<script>function myFunction()" \
               "{alert('You are not allowed access to this page!');}" \
               "</script><body onload='myFunction()'>"
    if request.method == 'POST':
        session.delete(blogPostToDelete)
        session.commit()
        return redirect(url_for('showBlog'))
    else:
        return render_template('deleteblogpost.html', blog=blogPostToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
