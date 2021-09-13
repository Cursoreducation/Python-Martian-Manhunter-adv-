from tests.conftest import client


def test_article_delete(client):
    response = client.delete("api/articles/13")
    assert response.status_code == 404
    response = client.get("api/articles/13")
    assert response.status_code == 404


def test_article_create(client):
    response = client.get("/article/create")
    data = response.json
    assert response.status_code == 200
    headers = {
        "Content-Type": "application/json"
    }

    json = {
        "title": "Cursor Education",
        "slug": "cursor education",
        "author_id": 1,
        "description": "Advanced python study course Advanced python study course Advanced python study course Advanced "
                       "python study course Advanced python study course",
        "short_description": "advanced python study course",
        "img": "https://www.zootovary.com/userfiles/482_1.jpg"
    }
    response = client.post('/article/store', headers=headers, json=json)
    assert response.status_code == 400


