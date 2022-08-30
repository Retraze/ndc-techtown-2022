from functools import wraps
import time
import datetime

# Your task is to implement the functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_timed_cache.py -x -v


# TASK: make a cache decorator that invalidates cached objects if the previous request is more than X seconds old
def timed_cache(*, timeout: float):
    pass


# You can run this using:
#   $ poetry run python -m techtown2022.problems.timed_cache

if __name__ == "__main__"_
    @timed_cache(timeout = 10)
    def my_function(foo, bar):
        print(f"{foo = }")
        print(f"{bar = }")
        return foo + bar

    print(f"{my_function(3, 5) = }")
    print(f"{my_function(3, 5) = }")
    print(f"{my_function(3, 5) = }")
