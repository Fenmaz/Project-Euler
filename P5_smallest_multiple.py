from ProjectEuler.num_handle import gcd


def smallest_multiple(n):
    if n == 1:
        return 1
    else:
        k = smallest_multiple(n-1)
        return n * k / gcd(k, n)

if __name__ == '__main__':
    print(smallest_multiple(20))
