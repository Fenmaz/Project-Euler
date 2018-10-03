def longest_collatz_sequence(n):
    steps = {1: 1}
    stack = []

    def next_collatz(num):
        if num % 2 == 0:
            return num // 2
        else:
            return 3 * num + 1

    for i in range(1, n + 1):
        if i % 10000 == 0:
            print(i // 10000, "%")
        if i not in steps:
            stack.append(i)
            while stack[-1] not in steps:
                stack.append(next_collatz(stack[-1]))
            last = steps[stack[-1]]
            count = 0
            for j in reversed(stack):
                steps[j] = last + count
                count += 1
            stack = []

    maximum = max(steps, key=lambda k: steps[k])
    return maximum

if __name__ == '__main__':
    print(longest_collatz_sequence(10 ** 6))
