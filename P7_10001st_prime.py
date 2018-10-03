from math import log
from ProjectEuler.prime_handle import create_prime_list


def find_nth_prime(n):
    assert n > 0
    if n < 13:
        return create_prime_list(100)[n-1]
    else:
        return create_prime_list(int(n * (log(n) + log(log(n)) - 1 + 1.8 * log(log(n))/log(n))) + 1)[n-1]

if __name__ == '__main__':
    print(find_nth_prime(10001))
