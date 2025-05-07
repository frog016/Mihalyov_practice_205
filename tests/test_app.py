import re
from datetime import datetime
from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that index route returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_page_content(client):
    """Test that page contains greeting text"""
    response = client.get('/')
    assert 'Привет'.encode('utf-8') in response.data

def test_date_format(client):
    """Test that date is in correct format"""
    response = client.get('/')
    data = response.data.decode('utf-8')
    date_match = re.search(r'\d{2}\.\d{2}\.\d{4}', data)
    assert date_match is not None
    current_date = datetime.now().strftime('%d.%m.%Y')
    assert current_date in data