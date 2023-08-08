from unittest.mock import Mock

import pytest
from src.exceptions import DatabaseError
from src.model import Customer

from src.repository import PureSQLRepository


def repo_with_mocked_cursor():
    db_mock_cursor = Mock()
    repository = PureSQLRepository(db_mock_cursor)
    return db_mock_cursor, repository


class TestPureSQLRepository:
    def test_save_customer(self):
        db_mock_cursor, repository = repo_with_mocked_cursor()
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        repository.save(customer)
        db_mock_cursor.execute.assert_called_once_with(
            """INSERT INTO {}(first_name,last_name, email) VALUES ({},{},{})""".format(
                repository.db_table_name,
                customer.first_name,
                customer.last_name,
                customer.email,
            )
        )

    def test_save_handle_db_exception_and_log_error(self, caplog):
        db_mock_cursor, repository = repo_with_mocked_cursor()
        db_mock_cursor.execute.side_effect = Mock(side_effect=Exception("Test"))
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        with pytest.raises(DatabaseError, match="Test"):
            repository.save(customer)
        for record in caplog.records:
            assert record.levelname == "CRITICAL"
        assert "Test" in caplog.text
