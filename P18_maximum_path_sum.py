def read_input(filename):
    f = open(filename)
    lines = []
    for line in f:
        lst = [int(i) for i in line.split()]
        lines.append(lst)
    return lines


def max_path_sum(rows):

    for row_i in range(1, len(rows)):
        rows[row_i][0] += rows[row_i - 1][0]
        rows[row_i][-1] += rows[row_i - 1][-1]
        for ele_i in range(1, row_i):
            prev_sum_left = rows[row_i - 1][ele_i - 1]
            prev_sum_right = rows[row_i - 1][ele_i]
            rows[row_i][ele_i] += max(prev_sum_left, prev_sum_right)

    return max(rows[-1])

if __name__ == '__main__':
    inp = read_input("18_maximum_path_sum.txt")
    print(max_path_sum(inp))
