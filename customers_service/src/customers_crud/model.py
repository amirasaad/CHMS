"""model.py
"""
import json
import re
from dataclasses import asdict, dataclass
from typing import Optional, Tuple


@dataclass
class Customer:
    """Customer model.

    Raises:
        ValueError: For invalid inputs

    """

    first_name: str
    last_name: str
    email: str
    # pylint: disable-next=invalid-name
    id: Optional[int] = None  # noqa: C0103

    EMAIL_INVALID = "Invalid email."
    EMAIL_REQUIRED = "email is required."
    FIRST_NAME_REQUIRED = "first_name is required."
    LAST_NAME_REQUIRED = "last_name is required."

    @staticmethod
    def from_row(customer_row: Tuple[int, str, str, str]):
        """Convert from database record to customer object.

        Args:
            customer_row (Tuple[int, str, str, str]): Customer row in database.

        Returns:
            Customer: object
        """
        return Customer(
            id=customer_row[0],
            first_name=customer_row[1],
            last_name=customer_row[2],
            email=customer_row[3],
        )

    def to_json(self):
        """Convert to json.

        Returns:
            dict: customer json
        """
        return json.dumps(asdict(self))

    def __post_init__(self):
        # Validate empty
        if not self.first_name:
            raise ValueError(self.FIRST_NAME_REQUIRED)
        if not self.last_name:
            raise ValueError(self.LAST_NAME_REQUIRED)
        if not self.email:
            raise ValueError(self.EMAIL_REQUIRED)
        # Validate email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError(self.EMAIL_INVALID)
