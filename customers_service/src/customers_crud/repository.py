"""repository.py
"""
import logging
from abc import ABC, abstractmethod

from .exceptions import DatabaseError
from .model import Customer

logger = logging.getLogger(__name__)


class CustomerRepository(ABC):
    """Abstract Repository."""

    @abstractmethod
    def save(self, customer: Customer):
        """Persist customer in database

        Args:
            customer (Customer): customer object to be persisted.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: int):
        """Get customer by id form database.

        Args:
            customer_id (int): customer id to be retrieved.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, customer_id: int, customer_dict: dict):
        """Update existing customer in database.

        Args:
            customer_id (int): customer id.
            customer_dict (dict): containing customer data to be updated.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, customer_id: int):
        """Delete customer from the database.

        Args:
            customer_id (int): customer id in database.

        """
        raise NotImplementedError


class MySQLRepository(CustomerRepository):
    """Mysql implementation for ABCRepository."""

    def __init__(self, db_connection, db_table_name: str = "Customers"):
        self.db_connection = db_connection
        self.db_table_name = db_table_name

    def save(self, customer: Customer):
        """Save customer information into the database.

        Args:
            customer (Customer): Holds valid customer information to be saved into the database.

        Raises:
            DatabaseError: Any exceptions caught during the delete will raised
            a DatabaseError from that exception.

        Returns:
            int: ID of the saved customer in the database.
        """
        cursor = self.db_connection.cursor()
        # pylint: disable-next=line-too-long
        sql = f"""INSERT INTO {self.db_table_name} (first_name, last_name, email) VALUES (%s,%s,%s)"""  # noqa
        try:
            cursor.execute(
                sql,
                (
                    customer.first_name,
                    customer.last_name,
                    customer.email,
                ),
            )
        except Exception as error:
            raise DatabaseError(str(error)) from error
        self.db_connection.commit()
        # Cursor lastrowid holds the last row's id.
        return cursor.lastrowid

    def get(self, customer_id: int):
        cursor = self.db_connection.cursor()
        # pylint: disable-next=line-too-long
        sql = f"""SELECT id,first_name,last_name,email from {self.db_table_name} WHERE id = {customer_id}"""
        try:
            cursor.execute(sql)
        except Exception as error:
            raise DatabaseError(str(error)) from error
        customer_db = cursor.fetchone()
        return Customer.from_row(customer_db)

    def update(self, customer_id: int, customer_dict: dict):
        """Update customer information in the database for a given dict.

        Args:
            customer_id (int): Customer ID to be updated.
            customer_dict (dict): A dictionary of customer information to update from.

        Raises:
            DatabaseError: Any exceptions caught during the delete will raised
            a DatabaseError from that exception.
        """
        cursor = self.db_connection.cursor()
        update_fields = " = %s, ".join(customer_dict.keys())
        sql = f"""UPDATE {self.db_table_name} SET {update_fields} = %s WHERE id = %s"""
        try:
            cursor.execute(
                sql,
                tuple(customer_dict.values()) + (customer_id,),
            )
        except Exception as error:
            raise DatabaseError(str(error)) from error
        self.db_connection.commit()

    def delete(self, customer_id: int):
        """Delete a customer from the database by id.

        Args:
            customer_id (int): Customer id to delete.

        Raises:
            DatabaseError: Any exceptions caught during the delete will raised
            a DatabaseError from that exception.
        """
        cursor = self.db_connection.cursor()
        sql = f"""DELETE FROM {self.db_table_name} WHERE id = %s"""
        try:
            cursor.execute(sql, (customer_id,))
        except Exception as error:
            raise DatabaseError(str(error)) from error
        self.db_connection.commit()
