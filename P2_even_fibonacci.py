def sum_even_fib_numbers(n):
    fib = [1, 1]
    k = 2
    result = 0
    while fib[1] < n + 1:
        fib = [fib[1], fib[0] + fib[1]]
        k += 1
        if k == 3:
            k = 0
            result += fib[1]
    return result

if __name__ == '__main__':
    print(sum_even_fib_numbers(4 * (10 ** 6)))
