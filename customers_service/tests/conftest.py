from unittest.mock import MagicMock
import pytest


@pytest.fixture(scope="function")
def db_cursor():
    yield MagicMock()


@pytest.fixture(scope="function")
def db_connection(db_cursor):
    db_mock_connection = MagicMock()
    db_mock_connection.cursor.return_value = db_cursor
    yield db_mock_connection
