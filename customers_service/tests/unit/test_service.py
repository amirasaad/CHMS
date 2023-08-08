from unittest.mock import Mock
from customers_crud.services import (
    create_customer,
    update_customer,
    delete_customer,
    get_customer,
)
from customers_crud.repository import PureSQLRepository


def test_create_customer_service(db_connection):
    repo = PureSQLRepository(db_connection)
    customer_id = create_customer("John", "Smith", "joe@example.com", repo)
    assert customer_id != None


def test_update_customer_service(db_connection):
    repo = PureSQLRepository(db_connection)
    update_customer(1, "John", "Smith", "joe@example.com", repo)


def test_delete_customer_service(db_connection):
    repo = PureSQLRepository(db_connection)
    delete_customer(1, repo)


def test_get_customer_service(db_connection, db_cursor):
    repo = PureSQLRepository(db_connection)
    db_cursor.fetchone.return_value = {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@example.com",
    }
    customer = get_customer(1, repo)
    assert customer
