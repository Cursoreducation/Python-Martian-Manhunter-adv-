from tests.conftest import client


def test_menu_items(client):
    response = client.get('/menu_items')
    data = response.json()
    assert response.status_code == 200
    assert data['items']['name'] == 'Articles'