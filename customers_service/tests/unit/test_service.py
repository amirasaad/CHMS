from unittest.mock import Mock

import pytest

from customers_crud.exceptions import DatabaseError
from customers_crud.repository import PureSQLRepository
from customers_crud.services import (
    create_customer,
    delete_customer,
    get_customer,
    update_customer,
)


class TestCreateCustomer:
    def test_create_customer_service(self, db_connection):
        repo = PureSQLRepository(db_connection)
        customer_id = create_customer("John", "Smith", "joe@example.com", repo)
        assert customer_id != None

    def test_handle_database_error(self, caplog, db_connection, db_cursor):
        repo = PureSQLRepository(db_connection)
        db_cursor.execute.side_effect = Exception("Test")
        assert not create_customer("John", "Smith", "joe@example.com", repo)
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text


class TestUpdateCustomer:
    def test_update_customer_service(self, db_connection):
        repo = PureSQLRepository(db_connection)
        assert update_customer(customer_id=1, first_name="John", last_name="Smith", email="joe@example.com", repo=repo)

    def test_handle_database_error(self, caplog, db_connection, db_cursor):
        repo = PureSQLRepository(db_connection)
        db_cursor.execute.side_effect = Exception("Test")
        assert not update_customer(
            customer_id=1, first_name="John", last_name="Smith", email="joe@example.com", repo=repo
        )
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text

    def test_partial_update(self, db_connection):
        repo = PureSQLRepository(db_connection)
        assert update_customer(customer_id=1, email="test@example.com", repo=repo)


class TestDeleteCustomer:
    def test_delete_customer_service(self, db_connection):
        repo = PureSQLRepository(db_connection)
        assert delete_customer(1, repo)

    def test_handle_database_error(self, caplog, db_connection, db_cursor):
        repo = PureSQLRepository(db_connection)
        db_cursor.execute.side_effect = Exception("Test")
        assert not delete_customer(1, repo)
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text


class TestGetCustomer:
    def test_get_customer_service(self, db_connection, db_cursor):
        repo = PureSQLRepository(db_connection)
        db_cursor.fetchone.return_value = (
            1,
            "John",
            "Doe",
            "test@example.com",
        )
        assert get_customer(1, repo)

    def test_handle_database_error(self, caplog, db_connection, db_cursor):
        repo = PureSQLRepository(db_connection)
        db_cursor.execute.side_effect = Exception("Test")
        assert not get_customer(1, repo)
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text
