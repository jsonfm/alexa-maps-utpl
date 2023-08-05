"""jwt utils."""

import jwt
import time


def is_token_expired(access_token: str):
    if access_token is None:
        return False
    """Verifies if an `access_token` has expired."""
    try:
        decoded_token = jwt.decode(
            access_token, verify=False, algorithms=["HS256"],  options={"verify_signature": False})
        expiration_timestamp = decoded_token.get('exp', 0)
        current_timestamp = int(time.time())
        return expiration_timestamp <= current_timestamp
    except:
        return False
