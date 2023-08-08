import logging

from customers_crud.exceptions import DatabaseError
from .model import Customer

logger = logging.getLogger(__name__)


def create_customer(first_name: str, last_name: str, email: str, repo):
    customer = Customer(first_name=first_name, last_name=last_name, email=email)
    try:
        return repo.save(customer)
    except DatabaseError as e:
        logger.critical(str(e))
        return False

def update_customer(
    customer_id: int, first_name: str, last_name: str, email: str, repo
):
    try:
        repo.update(
            customer_id,
            {"first_name": first_name, "last_name": last_name, "email": email},
        )
    except DatabaseError as e:
        logger.critical(str(e))
        return False
    return True


def delete_customer(customer_id: int, repo):
    try:
        repo.delete(customer_id)
    except DatabaseError as e:
        logger.critical(str(e))
        return False
    return True

def get_customer(customer_id: int, repo):
    try:
        customer = repo.get(customer_id)
    except DatabaseError as e:
        logger.critical(str(e))
        return None
    return customer
