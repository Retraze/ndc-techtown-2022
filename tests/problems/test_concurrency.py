import techtown2022.problems.threading as problems
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import queue

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_concurrency.py -x -v


def test_threaded_map():
    threads = []
    def worker(value):
        time.sleep(0.1)
        threads.append(threading.get_ident())
        return value + 50
    assert [*problems.threaded_map(worker, 8, range(16))] == [*range(50, 66)], \
        "output is incorrect"
    assert len(set(threads)) > 1, "no threading took place"


def test_process_with_lock():
    q = queue.Queue(maxsize=1)
    def worker(a, b):
        assert q.empty()
        q.put_nowait(threading.get_ident())
        time.sleep(0.1)
        assert q.get_nowait() == threading.get_ident()
        return a + b

    with ThreadPoolExecutor(max_workers=8) as p:
        *out, = p.map(problems.process_with_lock, [worker]*16, range(16), range(10, 26))
    assert out == [i+i+10 for i in range(16)]


def test_submit_doubles():
    expected = [12, 6, 10, 14]
    class Pool:
        def submit(self, f, *a, **kw):
            assert not a,  "Please do not submit positional args"
            assert not kw, "Please do not submit keyword args"
            assert f(*a, **kw) == expected.pop(0), "return value is wrong"
    problems.submit_doubles(Pool(), [6, 3, 5, 7])
    assert expected == []
