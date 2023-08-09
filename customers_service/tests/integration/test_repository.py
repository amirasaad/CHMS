from unittest.mock import MagicMock, Mock

import pytest

from customers_crud.exceptions import DatabaseError
from customers_crud.model import Customer
from customers_crud.repository import MySQLRepository


class TestPureSQLRepository:
    def test_save_customer(self, db_connection, db_cursor):
        repository = MySQLRepository(db_connection)
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        id = repository.save(customer)
        db_cursor.execute.assert_called_once_with(
            """INSERT INTO {} (first_name, last_name, email) VALUES (%s,%s,%s)""".format(
                repository.db_table_name
            ),
            (customer.first_name, customer.last_name, customer.email),
        )
        db_connection.commit.assert_called_once()
        assert id != 1

    def test_save_handle_db_exception(self, db_connection, db_cursor):
        repository = MySQLRepository(db_connection)
        db_cursor.execute.side_effect = Exception("Test")
        customer = Customer(
            first_name="John", last_name="Smith", email="john@example.com"
        )
        with pytest.raises(DatabaseError, match="Test"):
            repository.save(customer)

    def test_get_customer_by_id(self, db_connection, db_cursor):
        repository = MySQLRepository(db_connection)
        customer_row = (
            1,
            "John",
            "Smith",
            "john@example.com",
        )
        db_cursor.fetchone.return_value = customer_row
        db_customer = repository.get(customer_id=1)
        db_cursor.execute.assert_called_once_with(
            """SELECT id,first_name,last_name,email from Customers WHERE id = 1"""
        )
        db_cursor.fetchone.assert_called_once()
        assert Customer.from_row(customer_row) == db_customer

    def test_delete_customer_by_id(self, db_connection, db_cursor):
        repository = MySQLRepository(db_connection)
        repository.delete(customer_id=1)
        db_cursor.execute.assert_called_once_with(
            """DELETE FROM Customers WHERE id = %s""",
            (1,),
        )
        db_connection.commit.assert_called_once()

    def test_update_customer_by_id(self, db_connection, db_cursor):
        repository = MySQLRepository(db_connection)
        customer_dict = {
            "first_name": "John",
            "last_name": "Smith",
            "email": "john@example.com",
        }
        repository.update(1, customer_dict)
        db_cursor.execute.assert_called_once_with(
            """UPDATE {} SET first_name = %s, last_name = %s, email = %s WHERE id = %s""".format(
                repository.db_table_name
            ),
            (
                customer_dict["first_name"],
                customer_dict["last_name"],
                customer_dict["email"],
                1,
            ),
        )

        db_connection.commit.assert_called_once()
