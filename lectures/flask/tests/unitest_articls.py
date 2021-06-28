import unittest
# from conftest import client
from app import app
import os
import tempfile
from flask import Flask



def client():
    with app.test_client() as client:
        yield client


class TestArticle(unittest.TestCase):

    def test_article_create(client):
        response = client.get('/article/create')
        data = response.json
        assert data.status_code == 200

        headers = {
            "Content-Type": "application/json"
        }

        json = {
            "title": "Test Article",
            "img": "https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg",
            "short_description": "bla bla bla bla bla bla bla bla bla",
            "description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla",
            "slug": "test-article",
            "author_id": "1"
        }
        response = client.post("/article/store", headers=headers, json=json)
        assert response.status_code == 500

    def test_delete_article(client):
        response = client.delete("api/articles/1")
        assert response.status_code == 204
        response = client.get("/api/articles/1")
        assert response.status_code == 404