def fibonacci():
    yield 0
    yield 1
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


if __name__ == '__main__':
    for i, ele in enumerate(fibonacci()):
        if ele > 10 ** 999:
            print(i)
            break
