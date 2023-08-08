from unittest.mock import Mock
from customers_crud.services import (
    create_customer,
    update_customer,
    delete_customer,
    get_customer,
)
from customers_crud.repository import PureSQLRepository
from ..unit.test_repository import repo_with_mocked_cursor


def test_create_customer_service():
    repo = PureSQLRepository(Mock())
    customer_id = create_customer("John", "Smith", "joe@example.com", repo)
    assert customer_id != None


def test_update_customer_service():
    repo = PureSQLRepository(Mock())
    update_customer(1, "John", "Smith", "joe@example.com", repo)


def test_delete_customer_service():
    repo = PureSQLRepository(Mock())
    delete_customer(1, repo)


def test_get_customer_service():
    repo, mock_cursor, db_mock_connection = repo_with_mocked_cursor()
    mock_cursor.fetchone.return_value = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@example.com",
    }
    customer = get_customer(1, repo)
    assert customer
