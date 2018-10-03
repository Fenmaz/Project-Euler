def gcd(n, m):
    if n < m:
        n, m = m, n
    k = n % m
    while k != 0:
        n, m = m, k
        k = n % m
    return m


def find_divisor(n):
    divisors = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 2
    return divisors


def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
