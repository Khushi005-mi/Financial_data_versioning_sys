import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())
def generate_time_uuid() -> str:
    return str(uuid.uuid1())
import secrets
import string


def generate_public_id(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

