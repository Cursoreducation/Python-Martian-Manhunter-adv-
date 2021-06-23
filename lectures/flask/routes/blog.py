from app import app, api, db
from flask import render_template, request, Response
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


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


class Articles(Resource):
    def post(self):
        data = request.json
        article = Article(
            title=data.get('title'),
            slug=data.get('slug'),
            author_id=data.get('author_id'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            img=data.get('img')
        )
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def get(self):
        articles = Article.query
        if request.args.get('title'):
            articles = articles.filter_by(title=request.args.get('title'))

        # articles = articles.filter(Article.title.startswith('A'))

        if request.args.get("sort_by"):
            articles = articles.order_by(request.args.get("sort_by"))

        articles = articles.all()
        serialized_articles = []
        for article in articles:
            serialized_articles.append(article.serialize)

        return serialized_articles


class ArticlesEntity(Resource):
    def get(self, id):
        article = Article.query.get(id)
        if article == None:
            return Response(status=404)
        return article.serialize


class Users(Resource):
    # add
    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            created=data.get('created'),
            bio=data.get('bio'),
            admin=data.get('admin'),
        )
        db.session.add(user)
        db.session.commit()
        return user.serialize

    # View All
    def get(self):
        users = User.query
        serialized_users = []
        for user in users.all():
            print(user)
            serialized_users.append(user.serialize)
        return serialized_users


class UserModify(Resource):
    # View One
    def get(self, id):
        user = User.query.get(id)
        if user is None:
            return Response(status=404)
        return user.serialize

    # Update
    def put(self, id):
        data = request.json
        user = User.query.get(id)
        if user is None:
            return Response(status=404)
        else:
            user.username = data.get('username')
            user.email = data.get('email')
            user.created = data.get('created')
            user.bio = data.get('bio')
            user.admin = data.get('admin')
            db.session.commit()
            return user.serialize


api.add_resource(MenuItem, '/menu-items')
api.add_resource(Articles, '/articles')
api.add_resource(Users, '/users')
api.add_resource(UserModify, '/users/<int:id>')
api.add_resource(ArticlesEntity, '/articles/<int:id>')
