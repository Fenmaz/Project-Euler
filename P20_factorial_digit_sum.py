from ProjectEuler.num_handle import factorial


def strip_zeros(n):
    while n % 10 == 0:
        n //= 10
    return n


def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    fac = strip_zeros(factorial(100))
    print(sum_digit(fac))
