def proper_divisor_sums(n):
    divisors_sum = [0 for _ in range(n)]
    for i in range(1, n):
        k = i * 2
        while k < n:
            divisors_sum[k] += i
            k += i
    return divisors_sum


def abundant_num_list(n):
    divisors_sum = proper_divisor_sums(n)
    abundant_list = []
    for i, div_sum in enumerate(divisors_sum):
        if div_sum > i:
            abundant_list.append(i)
    return abundant_list


def non_abundant_sum(n):
    abundant_num = abundant_num_list(n)
    abundant_summable = [False for _ in range(n)]
    for i, num in enumerate(abundant_num):
        for num2 in abundant_num[i:]:
            if num + num2 >= n:
                break
            abundant_summable[num + num2] = True

    total = 0
    for i, summable in enumerate(abundant_summable):
        if not summable:
            total += i
    return total


if __name__ == '__main__':
    print(non_abundant_sum(28123))
