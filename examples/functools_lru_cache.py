import functools
import time

def fibonacci_no_cache(x):
    if x == 0: return 1
    if x == 1: return 1
    return fibonacci_no_cache(x-2) + fibonacci_no_cache(x-1)

@functools.lru_cache
def fibonacci_with_cache(x):
    if x == 0: return 1
    if x == 1: return 1
    return fibonacci_with_cache(x-2) + fibonacci_with_cache(x-1)

for func, args in [
    (fibonacci_no_cache,   [1]),
    (fibonacci_no_cache,   [10]),
    (fibonacci_no_cache,   [11]),
    (fibonacci_no_cache,   [12]),
    (fibonacci_no_cache,   [13]),
    (fibonacci_no_cache,   [21]),
    (fibonacci_with_cache, [1]),
    (fibonacci_with_cache, [10]),
    (fibonacci_with_cache, [11]),
    (fibonacci_with_cache, [12]),
    (fibonacci_with_cache, [13]),
    (fibonacci_with_cache, [100]),
    (fibonacci_with_cache, [500]),
]:
    t = time.perf_counter_ns()
    func(*args)
    print(f"{func.__name__:<20}{tuple(args)!r:<6} took {time.perf_counter_ns() - t:>10} ns")

    fibonacci_with_cache.cache_clear()
