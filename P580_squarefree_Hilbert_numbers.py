def main(n):

    print("Initializing...")

    h_num = (n + 3) // 4
    sqr_root = int(h_num ** 0.5)
    squarefree = {i: True for i in range(h_num)}

    print("Running the loop...")

    for i in range(1, sqr_root + 1):
        num = 4*i + 1
        sqr = num * num
        k = sqr
        while k < n:
            squarefree[(k - 1) // 4] = False
            k += 4 * sqr

    print("Returning result...")

    return sum(squarefree.values())

if __name__ == '__main__':
    print(main(10 ** 16))
