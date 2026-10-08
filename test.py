import os
password = os.environ.get("PASSWORD")


def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
