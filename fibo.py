from functools import lru_cache


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n-1) + fib1(n-2)


old = fib1

#
#
# cache = {}
#
#
# def fib2(n):
#     assert n >= 0
#     if n not in cache:
#         cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
#     return cache[n]
#


def memo(f):
    cache = {}

    def inner(n):
        assert n >= 0
        if n not in cache:
            cache[n] = n if n <= 1 else inner(n-1) + inner(n-2)
        return cache[n]
    return inner


fib1 = memo(old)
print(fib1(8000))


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib3(8000))


