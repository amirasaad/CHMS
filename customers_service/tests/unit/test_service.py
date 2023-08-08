from unittest.mock import Mock
from ...src.services import create_customer
from ...src.repository import PureSQLRepository


def test_create_customer_service():
    repo = PureSQLRepository(Mock())
    id = create_customer("John", "Smith", "joe@example.com", repo)
    assert id != None
