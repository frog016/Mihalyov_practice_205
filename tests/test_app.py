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