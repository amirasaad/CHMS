from dataclasses import asdict, dataclass
import json
from typing import Optional


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str
    id: Optional[int] = None

    @staticmethod
    def from_dict(customer_dict):
        return Customer(
            id=customer_dict["id"],
            first_name=customer_dict["first_name"],
            last_name=customer_dict["last_name"],
            email=customer_dict["email"],
        )

    def to_json(self):
        return json.dumps(asdict(self))
