from time import perf_counter_ns, sleep
from statistics import mean

# Your task is to implement the functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_timeit.py -x -v


# TASK: make a decorator that runs the decorated function 30 times and computes the mean execution time in nanosecond
def timeit(func: callable) -> float:
    pass



# You can run this using:
#   $ poetry run python -m python_properly.problems.timeit

if __name__ == "__main__":
    @timeit
    def something_slow():
        sleep(3 / 30)

    print(something_slow)
