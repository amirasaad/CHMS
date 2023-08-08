from mysql.connector import connection

from . import config

db_connection = connection.MySQLConnection(
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    database=config.DB_NAME,
)
