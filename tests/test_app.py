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
    """Тест проверяет доступность главной страницы"""
    response = client.get('/')
    assert response.status_code == 200

def test_page_content(client):
    """Тест проверяет наличие базового текста на странице"""
    response = client.get('/')
    assert b'Привет' in response.data

def test_date_format(client):
    """Тест проверяет корректность формата даты"""
    response = client.get('/')
    data = response.data.decode('utf-8')
    
    # Ищем дату в формате ДД.ММ.ГГГГ
    date_match = re.search(r'\d{2}\.\d{2}\.\d{4}', data)
    assert date_match is not None
    
    # Проверяем, что дата соответствует текущей
    current_date = datetime.now().strftime('%d.%m.%Y')
    assert current_date in data