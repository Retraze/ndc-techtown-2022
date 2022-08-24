from functools import wraps
import time
import datetime

# Your task is to implement the functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_timed_cache.py -x -v


# TASK: make a cache decorator that invalidates cached objects if the previous request is more than X seconds old
def timed_cache(*, timeout: float):
    pass
