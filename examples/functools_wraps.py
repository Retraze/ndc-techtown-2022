from functools import wraps
from pprint import pprint

def example_decorator(func):
    def wrapper(*a, **kw):
        """this is the doc-string for `wrapper`"""
        return func(*a, **kw)
    return wrapper

@example_decorator
def make_triplet(a: int, b: float, c: str) -> tuple[int, float, str]:
    """this is the doc-string for `make_triplet`"""
    return (a, b, c)

print(make_triplet.__name__)
print(make_triplet.__doc__)
pprint(make_triplet.__annotations__)


print()
print("="*20)
print()


def example_decorator(func):
    @wraps(func)
    def wrapper(*a, **kw):
        """this is the doc-string for `wrapper`"""
        return func(*a, **kw)
    return wrapper

@example_decorator
def make_triplet(a: int, b: float, c: str) -> tuple[int, float, str]:
    """this is the doc-string for `make_triplet`"""
    return (a, b, c)

print(make_triplet.__name__)
print(make_triplet.__doc__)
pprint(make_triplet.__annotations__)
