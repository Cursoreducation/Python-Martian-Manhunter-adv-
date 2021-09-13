import datetime
import os
from app import app, api, db
from flask import render_template, request, Response, redirect
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    return render_template('blog/details.html', article=article)


@app.route('/article/create')
def article_create():
    return render_template('blog/article_create.html')


@app.route('/article/store', methods=["POST"])
def article_store():
    data = request.form
    img = request.files['img']
    if img:
        img.save(os.path.join(Config.UPLOAD_PATH, img.filename))
        path = "/" + Config.UPLOAD_PATH + img.filename

    article = Article(
        title=data.get('title'),
        slug=data.get('slug'),
        author_id=1,
        description=data.get('description'),
        short_description=data.get('short_description'),
        img=path
    )
    
    db.session.add(article)
    db.session.commit()
    return redirect("/")


@app.route('/user/registration')
def user_registration():
    return render_template('blog/user_registration.html')


@app.route('/user/user_created', methods=["POST"])
def user_create():
    data = request.form
    user = User(
        username=data.get('username'),
        email=data.get('email'),
        bio=data.get('bio'),
        created=datetime.date.today().strftime('%Y-%m-%d-%H:%M:%S'),
        admin=False
    )
    db.session.add(user)
    db.session.commit()
    return redirect("/")

