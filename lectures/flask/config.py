import os


class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    WEATHER_API_URL = os.environ.get("WEATHER_API_URL")
    WEATHER_API_HOST = os.environ.get("WEATHER_API_HOST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    BLOG_TITLE = {
        "name": "Blog Cursor",
        "description": "This blog was made in homework number 15"
    }
    MENU_ITEMS = [
        {
            'name': "Articles",
            'link': '/articles',
        },
        {
            'name': "Categories",
            'link': '/categories',
        },
    ]
    FOOTER_LINKS = [
                {
                    "name": "Setting",
                    "link": "/setting",
                },
                {
                    "name": "About us",
                    "link": "/about-us",
                },
                {
                    "name": "Help",
                    "link": "/help",
                },
    ]
    FOOTER_INFO = {
        "address": "ZAMARSTYNIVSKA 79, LVIV",
        "mob-tel": "+38 (067) 527 41 31",
        "email": "cursor@gmail.com"
    }




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


