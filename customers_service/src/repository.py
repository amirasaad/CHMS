# repository.py

from src.model import Customer


class PureSQLRepository:
    def __init__(self, db_cursor, db_table_name: str = "Customers"):
        self.db_cursor = db_cursor
        self.db_table_name = db_table_name

    def save(self, customer: Customer):
        self.db_cursor.execute(
            """INSERT INTO {}(first_name,last_name, email) VALUES ({},{},{})""".format(
                self.db_table_name, customer.first_name, customer.last_name, customer.email
            )
        )
