"""jwt utils."""

import jwt
import time


def is_token_expired(access_token: str, secret_key: str):
    """Verifies if an `access_token` has expired."""
    try:
        decoded_token = jwt.decode(
            access_token, secret_key, algorithms=["HS256"])
        expiration_timestamp = decoded_token.get('exp', 0)
        current_timestamp = int(time.time())
        return expiration_timestamp <= current_timestamp
    except jwt.ExpiredSignatureError:
        return True
    except jwt.InvalidTokenError:
        return True
