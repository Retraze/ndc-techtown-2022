import python_properly.problems.list_comprehensions as problems
import random
import statistics
import functools
import more_itertools
import itertools

# you can run these tests like this:
#   $ poetry run pytest tests/problems/test_list_comprehensions.py -x -vv


# DATA

DATA = [random.randrange(10, 100) for _ in range(30)]

NESTED_DATA = [
    [random.randrange(10, 100) for _ in range(random.randrange(3, 8))]
    for _ in range(5)
]

MATRIX = [
    [random.randrange(10, 100) for _ in range(4)]
    for _ in range(4)
]


# tests

def test_compute_average():
    target = statistics.mean(DATA)
    assert problems.compute_average(DATA) == target


def test_compute_variance():
    target = statistics.pvariance(DATA)
    assert round(problems.compute_variance(DATA), 6) == round(target, 6)


def test_largest_element():
    target = functools.reduce(lambda a, b: a if a > b else b, DATA, 0)
    assert problems.largest_element(DATA) == target


def test_smallest_element():
    target = functools.reduce(lambda a, b: a if a < b else b, DATA, 9999999)
    assert problems.smallest_element(DATA) == target


def test_every_third():
    target = [i[0] for i in more_itertools.grouper(DATA, 3)]
    assert problems.every_third(DATA) == target


def test_even_only():
    *target, = itertools.filterfalse((1).__and__, DATA)
    assert problems.even_only(DATA) == target


def test_take_first_5():
    target, *_ = map(list, zip(*itertools.takewhile(lambda x: x[1]<5, zip(DATA,itertools.count(0)))))
    assert problems.take_first_5(DATA) == target


def test_reversed():
    _, target = map(list, zip(*sorted(zip(itertools.count(-3, -1), DATA))))
    assert problems.reversed(DATA) == target


def test_flatten():
    *target, = more_itertools.flatten(NESTED_DATA)
    assert problems.flatten(NESTED_DATA) == target


def test_transpose():
    *target, = zip(*itertools.zip_longest(*zip(*itertools.takewhile(lambda a: a[0]*10|1, zip(*itertools.takewhile(lambda a: len(a)*10|8, zip(*MATRIX)))))))
    assert problems.transpose(MATRIX) == target
