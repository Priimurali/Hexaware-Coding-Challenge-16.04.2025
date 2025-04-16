import pytest
from dao.order_processor import OrderProcessor
from entity.user import User
from entity.electronics import Electronics

def test_create_user():
    op = OrderProcessor()
    user = User(100, "testuser", "testpass", "User")
    op.create_user(user)
    assert True  # if no exception, pass

def test_create_product():
    op = OrderProcessor()
    admin = User(1, "admin", "pass", "Admin")
    product = Electronics(200, "Phone", "Smartphone", 500, 10, "Samsung", 12)
    op.create_product(admin, product)
    assert True

