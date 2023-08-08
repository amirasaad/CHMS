from unittest.mock import Mock
from src.model import Customer

from src.repository import PureSQLRepository

class TestPureSQLRepository:

    def test_save_customer(self):
        db_mock_cursor = Mock()
        repository = PureSQLRepository(db_mock_cursor)
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        repository.save(customer)
        db_mock_cursor.execute.assert_called_once_with(
            """INSERT INTO {}(first_name,last_name, email) VALUES ({},{},{})""".format(
                repository.db_table_name, customer.first_name, customer.last_name, customer.email
            )
        )

    def test_save_handle_db_exception(self):
        pass
