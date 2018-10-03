def read_input():
    f = open('13_large_sum.txt')
    return f.read().splitlines()


def large_sum(inputs):
    result = 0
    temp_sum = []
    for i in range(50):
        temp_sum.append(0)
        for j in inputs:
            temp_sum[i] += int(j[- i - 1])
    for i, j in enumerate(temp_sum):
        result += j * (10 ** i)
    return result


if __name__ == '__main__':
    inp = read_input()
    print(large_sum(inp))
