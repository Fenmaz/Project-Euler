def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def create_prime_list(n):
    if n <= 10:
        return [2, 3, 5, 7]
    else:
        sieve = [True for _ in range(n + 1)]
        sieve[0] = sieve[1] = False
        for i in create_prime_list(int(n ** 0.5)):
            j = i * 2
            while j < n + 1:
                sieve[j] = False
                j += i
        result = []
        for i in range(n + 1):
            if sieve[i]:
                result.append(i)
        return result
