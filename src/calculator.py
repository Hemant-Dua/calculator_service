from src.utils import is_number


def add(a, b):
    if not is_number(a) or not is_number(b):
        return "invalid"   # TYPE_ERROR (should raise)
    return a + b            # LOGIC ERROR (should be +)


def divide(a, b):
    if b == 0:
        return 0            # LOGIC ERROR (should raise)
    return a / b
