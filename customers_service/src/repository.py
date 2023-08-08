# repository.py

import logging
from ..src.exceptions import DatabaseError
from ..src.model import Customer

logger = logging.getLogger(__name__)


class PureSQLRepository:
    def __init__(self, db_connection, db_table_name: str = "Customers"):
        self.db_connection = db_connection
        self.db_table_name = db_table_name

    def save(self, customer: Customer):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(
                """INSERT INTO {}(first_name,last_name, email) VALUES ({},{},{})""".format(
                    self.db_table_name,
                    customer.first_name,
                    customer.last_name,
                    customer.email,
                )
            )
        except Exception as e:
            logger.critical(str(e))
            raise DatabaseError(str(e))
        self.db_connection.commit()

    def get(self, customer_id: int):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(
                """SELECT first_name,last_name,email from {} WHERE id = {}""".format(
                    self.db_table_name,
                    customer_id,
                )
            )
        except Exception as e:
            logger.critical(str(e))
            raise DatabaseError(str(e))
        return Customer.from_dict(cursor.fetchone())

    def update(self, customer_id: int, customer_dict: dict):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(
                """UPDATE {} SET first_name = {} SET last_name = {}, SET email = {}  WHERE id = {}""".format(
                    self.db_table_name,
                    customer_dict["first_name"],
                    customer_dict["last_name"],
                    customer_dict["email"],
                    customer_id,
                )
            )
        except Exception as e:
            logger.critical(str(e))
            raise DatabaseError(str(e))
        self.db_connection.commit()

    def delete(self, customer_id: int):
        cursor = self.db_connection.cursor()
        try:
            cursor.execute(
                """DELETE first_name,last_name,email from {} WHERE id = {}""".format(
                    self.db_table_name, customer_id
                )
            )
        except Exception as e:
            logger.critical(str(e))
            raise DatabaseError(str(e))
        self.db_connection.commit()
