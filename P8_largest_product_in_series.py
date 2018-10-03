def read_input():
    f = open('8_largest_product_in_a_series.txt')
    return f.read()


def largest_product(num, n):
    max_product = 0
    for i in range(len(num) - n):
        current_product = 1
        for j in num[i:i + n]:
            current_product *= int(j)
        if current_product > max_product:
            max_product = current_product
    return max_product

if __name__ == '__main__':
    inp = read_input()
    print(largest_product(inp, 13))
