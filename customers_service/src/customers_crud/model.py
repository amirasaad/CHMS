import json
from dataclasses import asdict, dataclass
import re
from typing import Tuple, Optional


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str
    id: Optional[int] = None

    @staticmethod
    def from_row(customer_row: Tuple[int, str, str, str]):
        return Customer(
            id=customer_row[0],
            first_name=customer_row[1],
            last_name=customer_row[2],
            email=customer_row[3],
        )

    def to_json(self):
        return json.dumps(asdict(self))
