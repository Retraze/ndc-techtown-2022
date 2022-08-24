import python_properly.problems.timeit as problems
import itertools
import time

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_timeit.py -x -v


def test_number_of_iterations():
    c = itertools.count(0)
    problems.timeit(c.__next__)
    assert next(c) == 30

def test_result():
    @problems.timeit
    def timeit_result():
        time.sleep(0.08)

    delta = 1_000_000
    assert 80_000_000-delta < timeit_result < 80_000_000+delta
