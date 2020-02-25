# Rabbit Production using recursion
# Fibonacci sequence is as follows:
# 1 + 1 = 2
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 5 = 8
# and so on
# Function must be 1. Fast 2. Clean


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Dictionary Cache
# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Since this is a recursive call
# fib(5) -> fib(4) + fib(3)
# fib(4) -> fib(3) + fib(2)
# fib(3) -> fib(2) + fib(1)
#
# And hence same function call is called repeatedly.
# This can be optimized using `Memorization`.
# -> Save the current result

fibonacii_cache = dict()


def fib_mem(n):
    # If the value is already present then return it
    if n in fibonacii_cache:
        return fibonacii_cache[n]

    # Compute the Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fib_mem(n - 1) + fib_mem(n - 2)

    # Cache the value and return it
    fibonacii_cache[n] = value
    return value


# - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LRU cache - Least Recently used cache
# - - - - - - - - - - - - - - - - - - - - - - - - - - -
from functools import lru_cache


@lru_cache(maxsize=1000)
def fib_lru(n):
    if n == 1 or n == 2:
        return 1
    return fib_lru(n - 1) + fib_lru(n - 2)


for i in range(1, 1001):
    print(i, " : ", fib(i))
