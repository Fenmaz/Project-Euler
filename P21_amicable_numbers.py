def proper_divisors_list(n):
    divisors = [[] for _ in range(n)]
    for i in range(1, n):
        k = i * 2
        while k < n:
            divisors[k].append(i)
            k += i
    return divisors


def find_amicable_total(divisors):
    n = len(divisors)
    sum_divisor = [sum(divisors[i]) for i in range(n)]
    total = 0
    for i in range(n):
        j = sum_divisor[i]
        if j != i and j < n and sum_divisor[j] == i:
            total += i
    return total


if __name__ == '__main__':
    print(find_amicable_total(proper_divisors_list(10000)))
