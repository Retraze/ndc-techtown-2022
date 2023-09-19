from concurrent.futures import ThreadPoolExecutor
import threading
import functools

# Your task is to implement the functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_concurrency.py -x -v


# TASK: process the elements of `data` in parallel, returning the result
def threaded_map(function: callable, min_workers: int, data: list) -> list:
    return [function(i) for i in data]


# TASK: make this function run `function(*inputs)` in a mutually exclusive way.
# i.e., make sure no two threads run `function` at the same time
lock = None
def process_with_lock(function: callable, *inputs):
    return function(*inputs)


# TASK: Fix this function, making sure each worker gets the correct arguments.
# This must be done using a closure or "bind"
def submit_doubles(pool: ThreadPoolExecutor, data: list):
    for i in data:
        @pool.submit
        def doubler():
            return i*2


# You can run this using:
#   $ poetry run python -m techtown2022.problems.concurrency

if __name__ == "__main__":
    class Pool():
        def submit(self, f):
            return f()

    print(f"{threaded_map((2).__add__, 5, [1, 2, 3, 4, 5]) = }")
    print(f"{process_with_lock(int.__add__, 3, 4)            = }")
    print(f"{submit_doubles(Pool(), [1, 2, 3, 4])          = }")
