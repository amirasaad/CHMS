"""Services crud.
"""
import logging

from .exceptions import DatabaseError
from .utils import validate_email

from .model import Customer
from .repository import ABCRepository

logger = logging.getLogger(__name__)


def create_customer(first_name: str, last_name: str, email: str, repo: ABCRepository):
    """Create customer service.

    Args:
        first_name (str):
        last_name (str):
        email (str):
        repo (Repository): A customer repository to handle database communication.

    Returns:
        int | bool: ID of the created customer if success otherwise False.
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
    """Update customer with non null given value

    Args:
        customer_id (int): ID of the customer in database.
        repo (ABCRepository): Customer Repository
        first_name (str | None, optional): _description_. Defaults to None.
        last_name (str | None, optional): _description_. Defaults to None.
        email (str | None, optional): _description_. Defaults to None.

    Returns:
        bool: True if success False otherwise
    """

    if email and not validate_email(email):
        raise ValueError(Customer.EMAIL_INVALID)
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
    """Delete customer from database

    Args:
        customer_id (int): ID of the customer in database.
        repo (ABCRepository): Customer Repository

    Returns:
       bool: True if success False otherwise
    """
    try:
        repo.delete(customer_id)
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return True


def get_customer(customer_id: int, repo: ABCRepository):
    """Get customer by ID from the database.

    Args:
        customer_id (int): ID of the customer in database.
        repo (ABCRepository): Customer Repository

    Returns:
        bool: True if success False otherwise
    """
    try:
        customer = repo.get(customer_id)
    except DatabaseError as error:
        logger.critical(str(error))
        return False
    return customer
