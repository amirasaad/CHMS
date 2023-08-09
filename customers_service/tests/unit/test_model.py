import pytest

from customers_crud.model import Customer


def test_validate_customer_email():
    with pytest.raises(ValueError, match=Customer.EMAIL_INVALID):
        Customer(first_name="test", last_name="test", email="test")


def test_validate_customer_empty_first_name():
    with pytest.raises(ValueError, match=Customer.FIRST_NAME_REQUIRED):
        Customer(first_name="", last_name="test", email="test")


def test_validate_customer_empty_last_name():
    with pytest.raises(ValueError, match=Customer.LAST_NAME_REQUIRED):
        Customer(first_name="test", last_name="", email="test")
