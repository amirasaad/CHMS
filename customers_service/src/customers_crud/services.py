"""Services crud.
"""
import logging

from customers_crud.exceptions import DatabaseError
from customers_crud.repository import ABCRepository

from .model import Customer

logger = logging.getLogger(__name__)


def create_customer(first_name: str, last_name: str, email: str, repo: ABCRepository):
    """Create customer service.

    Args:
        first_name (str):
        last_name (str):
        email (str):
        repo (Repository): A customer repository to handle database communication.

    Returns:
        int: ID of the created customer.
    """
    customer = Customer(first_name=first_name, last_name=last_name, email=email)
    logger.info("Saving %s to database", customer)
    try:
        customer_id = repo.save(customer)
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return customer_id


def update_customer(
    *,
    customer_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
    repo: ABCRepository
):
    customer_dict = {"first_name": first_name, "last_name": last_name, "email": email}
    # Remove None values
    customer_dict = {k: v for k, v in customer_dict.items() if v}
    try:
        repo.update(
            customer_id,
            customer_dict,
        )
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return True


def delete_customer(customer_id: int, repo: ABCRepository):
    try:
        repo.delete(customer_id)
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return True


def get_customer(customer_id: int, repo: ABCRepository):
    try:
        customer = repo.get(customer_id)
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return customer
