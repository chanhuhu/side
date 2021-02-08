import functools

@functools.lru_cache(maxsize=None)
def fibo(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

# 0 1 1 2 3 5 8 13 ..
for i in range(10):
    print(fibo(i))
