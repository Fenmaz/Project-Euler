def multiples_sum(n):
    lst = [False for _ in range(n)]
    result = 0
    k = 0
    while k < n:
        lst[k] = True
        k += 3
    k = 0
    while k < n:
        lst[k] = True
        k += 5
    for i, j in enumerate(lst):
        if j:
            result += i
    return result

if __name__ == '__main__':
    print(multiples_sum(1000))
