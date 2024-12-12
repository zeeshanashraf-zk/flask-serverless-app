import pytest
from app import app

# Flask app ka test client banayein
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test for "/" route
def test_hello_world(client):
    response = client.get('/')
    assert response.data == b"Hello, flask"
    assert response.status_code == 200

# Test for "/hello/<name>" route
def test_hello_name(client):
    response = client.get('/hello/John')
    assert response.data == b"Hello, John!"
    assert response.status_code == 200

# Test for "/goodbye" route
def test_goodbye(client):
    response = client.post('/goodbye')
    assert response.data == b"Goodbye, World!"
    assert response.status_code == 200
