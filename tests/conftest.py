import pytest

from shop import app, User
from shop.items.models import Item


@pytest.fixture(scope='session')
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def simple_user():
    return User(email='test@test.com', password='123')


@pytest.fixture(scope='module')
def admin_user():
    return User(email='test_admin@test.com', password='123', is_admin=True)


@pytest.fixture(scope='module')
def item():
    return Item(name='Test Item', price=1.99)
