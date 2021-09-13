import datetime
import os
from app import app, api, db, mail
from flask import render_template, request, Response, redirect, session
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from helpers.additional_functions import check_password
from flask_mail import Mail, Message


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    session['hello'] = 'hello world'
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/sign-up', methods=['GET'])
def sign_up():
    if session.get('user', False):
        return redirect('/')
    return render_template('blog/signup.html')


@app.route('/user-register', methods=['POST'])
def user_store():
    data = request.form
    user = User(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password'),
        location=data.get('location'),
        bio=data.get('description'),
        created=datetime.datetime.now(),
        admin=0,
    )

    db.session.add(user)
    db.session.commit()

    session['user'] = user.serialize
    return redirect("/")

#    msg = Message('Hello', sender='tredr02@gmail.com', recipients=[data.get('email')])
#    msg.html = render_template('blog/emails/activated.html', data=data)
#    mail.send(msg)
#    return render_template('blog/activate.html')


#@app.route('/activate/<string:email>')
#def activate(email):
#    user = User.query.filter_by(email=email).first()
#    user.activated = 1
#    db.session.commit()
#    session['user'] = user.serialize
#    return render_template('blog/activated.html')


@app.route('/sign-in', methods=['GET'])
def sign_in():
    if session.get('user', False):
        return redirect('/')
    return render_template('blog/signin.html')


@app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.form.get('username')).first()
    if user:
        if check_password(user.password, request.form.get('password')):
            user.location = request.form.get('location')
            db.session.commit()
            session['user'] = user.serialize
    else:
        user = User.query.filter_by(username=request.form.get('username')).first()
        if user:
            if check_password(user.password, request.form.get('password')):
                user.location = request.form.get('location'),
                db.session.commit()
                session['user'] = user.serialize

    return redirect('/')


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/details.html', article=article)


@app.route('/article/create')
def article_create():
    if not session.get('user', False):
        return redirect('/')
    return render_template('blog/article_create.html')


@app.route('/contact-us')
def contact_us():
    return render_template('blog/contact-us.html')


@app.route('/article/store', methods=["POST"])
def article_store():
    if not session.get('user', False):
        return redirect('/')
    data = request.form
    img = request.files['img']
    if img:
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))
        path = "/" + Config.UPLOAD_PATH + img.filename

    article = Article(
        title=data.get('title'),
        slug=data.get('slug'),
        author_id=1,
        location=data.get('location'),
        description=data.get('description'),
        short_description=data.get('short_description'),
        img=path
    )
    
    db.session.add(article)
    db.session.commit()
    return redirect("/")


#@app.route('/user/registration')
#def user_registration():
#    return render_template('blog/user_registration.html')


#@app.route('/user/user_created', methods=["POST"])
#def user_create():
#    data = request.form
#    user = User(
#        username=data.get('username'),
#        email=data.get('email'),
#        location=data.get('location'),
#        bio=data.get('bio'),
#        created=datetime.date.today().strftime('%Y-%m-%d-%H:%M:%S'),
#        admin=False
#    )
#    db.session.add(user)
#    db.session.commit()
#    return redirect("/")

