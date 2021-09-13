import os


class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    WEATHER_API_URL = os.environ.get("WEATHER_API_URL")
    WEATHER_API_HOST = os.environ.get("WEATHER_API_HOST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    UPLOAD_PATH = 'static/uploads/'
    BLOG_TITLE = "Blog Cursor"
    MENU_ITEMS = [
        {
            "name": "Articles",
            "link": "/articles",
        },
        {
            "name": "Categories",
            "link": "/categories",
        },
    ]

    FOOTER_LINKS = [
        {
            "name": "Info",
            "link": "/info"
        },
        {
            "name": "Home",
            "link": "/home"
        },
        {
            "name": "Help",
            "link": "/help",
        },
        {
            "name": "Contacts",
            "link": "/contacts",
        },
        {
            "name": "Docs",
            "link": "/docs"
        },
        {
            "name": "about us",
            "link": "/about_us",
        }
    ]


def articles():
    return [
        {
            "title": "Test Article",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article'
        },
        {
            "title": "Test Article2",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article2'
        },
    ]
