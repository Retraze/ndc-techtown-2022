import techtown2022.problems.timed_cache as problems
import pytest
import time

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_timed_cache.py -x -v

def test_timed_cache_timeout():

    @problems.timed_cache(timeout=0.3)
    def allow_only_once(_state=[]):
        if not _state:
            _state.append(None)
            return 5
        else:
            assert False, "The cache doesn't work as intended"

    for _ in range(50):
        assert allow_only_once() == 5

    time.sleep(0.5)

    with pytest.raises(AssertionError):
        allow_only_once()


def test_timed_cache_varargs():
    done = set()

    @problems.timed_cache(timeout=1000)
    def foo(*a, **kw):
        hash = (a, *sorted(kw.items()))
        assert hash not in done, "The decorator does not handle variable arguments"
        done.add(hash)
        return hash

    for _ in range(10):
        for a, kw in [
            ((), {}),
            (range(0, 10), dict(foo="bar")),
            (range(5, 10), dict(foo="bar")),
            (range(7, 10), dict(foo="bar", baz="Hello, World!")),
            (range(3, 10), dict(foo="bar", baz="Hello, World!")),
            (range(4, 10), dict(foo="bar", baz="Hello, World!")),
            (range(4, 10), dict(baz="Hello, World!", foo="bar")),
        ]:
            assert foo(*a, **kw)[0] == tuple(a)


@pytest.mark.timeout(4)
def test_timed_cache_fib():

    @problems.timed_cache(timeout=1000)
    def fib(n):
        if n == 0: return 1
        if n == 1: return 1
        return fib(n-1) + fib(n-2)

    assert fib(5)   == 8
    assert fib(50)  == 20365011074
    assert fib(100) == 573147844013817084101
    assert fib(500) == 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626


def test_wraps():

    @problems.timed_cache(timeout=50)
    def this_function_name_should_not_be_changed(the: "type", annotation: "should be") -> "properly":
        "the doc string should be preserved"

    assert this_function_name_should_not_be_changed.__name__ == "this_function_name_should_not_be_changed"
    assert this_function_name_should_not_be_changed.__doc__  == "the doc string should be preserved"
    assert this_function_name_should_not_be_changed.__annotations__  == {'the': 'type', 'annotation': 'should be', 'return': 'properly'}

    # make sure it is not hardcoded

    @problems.timed_cache(timeout=50)
    def this_name_is_also_important(a: int, b: float) -> str:
        "foo bar baz quz"

    assert this_name_is_also_important.__name__ == "this_name_is_also_important"
    assert this_name_is_also_important.__doc__  == "foo bar baz quz"
