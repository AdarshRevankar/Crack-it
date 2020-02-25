import time


# Check if integer is Prime
# Prime number is number divisible by itself or 1
#
# Eg: 2, 3, 5, 7, 11 .. etc
#
# Unit : 1

# Version 1


def is_prime_v1(n):
    """Return true if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False  # 1 is not prime

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


# version 2
# Logic:
# The prime number factor is as follows:
# 36 =  1 x 36  -+
#       2 * 18   |
#       3 * 12   |
#       4 * 9    |
#       6 * 6  --+
#       4 * 9    |
#       12 * 3   |
#       18 * 2   |
#       36 * 1 --+
# Here the number repeats after sqrt(n) * sqrt(n)
# Also, the number can be NOT A PERFECT SQUARE, works fine.
# This is used in V2
import math


def is_prime_v2(n):
    """Return true if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 10):
        if n % d == 0:
            return False
    return True


# version 3
# if input is even then it will be prime
# wasting into loop is not correct
# Hence we can save time

def is_prime_v3(n):
    """Return true if 'n' is a prime number. False otherwise"""

    if n == 1:
        return False

    # if n is even
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


# ===== Test Function =====
count = 0
N = 50000
t0 = time.time()
for i in range(1, N):
    count = count + 1 if is_prime_v2(i) == is_prime_v3(i) else count
t1 = time.time()
print("Time required : ", t1 - t0)
print((count/N) * 100);

# Pseudo Prime
