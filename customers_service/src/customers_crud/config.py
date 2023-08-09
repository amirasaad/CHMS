"""App config
"""
import os

DB_NAME = os.environ.get("MYSQL_DB", "car_rental_db")
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD", "sekret")
