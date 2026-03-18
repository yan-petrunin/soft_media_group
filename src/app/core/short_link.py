import secrets

def generate_short_id(length: int = 8) -> str:
    return secrets.token_urlsafe(length)[:length]
