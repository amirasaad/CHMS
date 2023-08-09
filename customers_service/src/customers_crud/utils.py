import re


def validate_email(email):
    """Check if email is valid."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
