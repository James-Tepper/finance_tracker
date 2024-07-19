import bcrypt


def hash_password(password: str) -> bytes:
    hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashword


def check_password(password: str, hashword: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode(), hashword.encode())
    except ValueError:
        return False
