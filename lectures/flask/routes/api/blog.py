from app import app, api, db, mail
from flask import render_template, request, Response
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from flask_mail import Message


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

    def delete(self, id):
        article = Article.query.get(id)

        if article == None:
            return Response(status=404)

        db.session.delete(article)
        db.session.commit()

        return Response(status=204)


class Users(Resource):
    def get(self):
        user = User.query.get(1)
        serialized_articles = []
        for article in user.articles:
            print(article)
            serialized_articles.append(article.serialize)
        return serialized_articles


class Contact(Resource):
    def post(self):
        data = request.json
        msg = Message('Contact form alert!', sender='turupuru8@gmail.com', recipients=['l.luzhnuy@gmail.com'])
        msg.html = "Contact Email: " + data['email'] + "<br>" + "Contact Title: " + data['title'] + "<br>" + "Contact Description: " + data['description']
        mail.send(msg)
        client_msg = Message('Dear Client!', sender='turupuru8@gmail.com', recipients=[data['email']])
        client_msg.html = render_template('blog/emails/contact.html', email=data['email'])
        mail.send(client_msg)
        return Response(status=200)


api.add_resource(MenuItem, '/api/menu-items')
api.add_resource(Articles, '/api/articles')
api.add_resource(Users, '/api/users')
api.add_resource(ArticlesEntity, '/api/articles/<int:id>')
api.add_resource(Contact, '/api/contact')
