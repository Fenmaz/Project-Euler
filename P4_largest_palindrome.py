def largest_palindrome_product(n):
    max_pal = 9
    for i in range(10 ** (n-1), 10 ** n):
        for j in range(10 ** (n-1), 10 ** n):
            if str(i * j) == str(i * j)[::-1] and i * j > max_pal:
                max_pal = i * j
    return max_pal

if __name__ == '__main__':
    print(largest_palindrome_product(3))
