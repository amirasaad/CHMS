from unittest.mock import MagicMock, Mock

import pytest
from ...src.exceptions import DatabaseError
from ...src.model import Customer

from ...src.repository import PureSQLRepository


def repo_with_mocked_cursor():
    db_mock_connection = MagicMock()
    repository = PureSQLRepository(db_mock_connection)
    mock_cursor = MagicMock()
    db_mock_connection.cursor.return_value = mock_cursor
    return repository, mock_cursor, db_mock_connection


class TestPureSQLRepository:
    def test_save_customer(self):
        repository, mock_cursor, db_mock_connection= repo_with_mocked_cursor()
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        repository.save(customer)
        mock_cursor.execute.assert_called_once_with(
            """INSERT INTO {}(first_name,last_name, email) VALUES ({},{},{})""".format(
                repository.db_table_name,
                customer.first_name,
                customer.last_name,
                customer.email,
            )
        )
        db_mock_connection.commit.assert_called_once()

    def test_save_handle_db_exception_and_log_error(self, caplog):
        repository, mock_cursor, _ = repo_with_mocked_cursor()
        mock_cursor.execute.side_effect = Exception("Test")
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        with pytest.raises(DatabaseError, match="Test"):
            repository.save(customer)
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text

    def test_repository_get_customer_by_id(self):
        repository, mock_cursor, _ = repo_with_mocked_cursor()
        customer_dict = {
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
        }
        mock_cursor.fetchone.return_value = customer_dict
        db_customer = repository.get(customer_id=1)
        mock_cursor.execute.assert_called_once_with(
            """SELECT first_name,last_name,email from Customers WHERE id = 1"""
        )
        mock_cursor.fetchone.assert_called_once()
        assert Customer.from_dict(customer_dict) == db_customer

    def test_repository_delete_customer_by_id(self):
        repository, mock_cursor, db_mock_connection = repo_with_mocked_cursor()
        repository.delete(customer_id=1)
        mock_cursor.execute.assert_called_once_with(
            """DELETE first_name,last_name,email from Customers WHERE id = 1"""
        )
        db_mock_connection.commit.assert_called_once()

    def test_repository_update_customer_by_id(self):
        repository, mock_cursor, db_mock_connection = repo_with_mocked_cursor()
        customer_dict = {
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
        }
        repository.update(1, customer_dict)
        mock_cursor.execute.assert_called_once_with(
            """UPDATE Customers SET first_name = {} SET last_name = {}, SET email = {}  WHERE id = 1""".format(
                customer_dict["first_name"],
                customer_dict["last_name"],
                customer_dict["email"],
            )
        )
        db_mock_connection.commit.assert_called_once()
