import functools
import time

def brench(func):
    def timed(*args, **kwargs):
        t0 = time.monotonic_ns()
        func(*args, **kwargs)
        t1 = time.monotonic_ns()
        return (t1 - t0) * 1e-9 # convert nanosecond to second
    return timed


@brench
@functools.lru_cache(maxsize=None)
def fibo(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

# 0 1 1 2 3 5 8 13 ..
for i in range(10000):
    print(fibo(i))
