from ProjectEuler.prime_handle import create_prime_list


def largest_prime_factor(n):
    prime_lst = create_prime_list(int(n ** 0.5))
    print('Completed creating prime list up to n ** 0.5. Testing n.')
    max_prime = 1
    k = 0
    while k != len(prime_lst):
        if n % prime_lst[k] == 0:
            max_prime = prime_lst[k]
            n //= prime_lst[k]
        else:
            k += 1
    if n != 1:
        print('Largest prime factor larger than n ** 0.5. Running largest_prime_factor_2')
        return largest_prime_factor_2(n)
    return max_prime


def largest_prime_factor_2(n):
    prime_lst = create_prime_list(n)
    print('Completed creating prime list up to current n. Testing new n.')
    for i in reversed(prime_lst):
        if n % i == 0:
            return i
    raise ValueError

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
