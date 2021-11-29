"""Data models."""
from app import db
from helpers.serializers import Serializer

class User(db.Model, Serializer):
    """Data model for user accounts."""
    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    password = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    bio = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )
    articles = db.relationship("Article", backref='author', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            'bio': self.bio,
        }


article_categories = db.Table('article_categories',
                        db.Column("article_id", db.Integer, db.ForeignKey('articles.id')),
                        db.Column("category_id", db.Integer, db.ForeignKey("category.id"))
                    )


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # author = db.relationship("User", backref='articles', lazy=True)
    title = db.Column(
        db.String(255),
        nullable=False,
        index=True,
        unique=False
    )
    slug = db.Column(
        db.String(50),
        nullable=False,
        index=True,
        unique=False
    )
    description = db.Column(
        db.Text,
        nullable=False,
        index=False,
        unique=False
    )
    short_description = db.Column(
        db.String(350),
        nullable=True,
        index=False,
        unique=False
    )
    img = db.Column(
        db.String(255),
        nullable=True,
        index=False,
        unique=False
    )
    categories = db.relationship("Category", secondary=article_categories, back_populates="articles")

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            'description': self.description,
            "short_description": self.short_description,
            "img": self.img
        }


class Category(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(350)
    )

    articles = db.relationship("Article", secondary=article_categories, back_populates="categories")
