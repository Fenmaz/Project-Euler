def read_input():
    f = open('11_largest_product_in_a_grid.txt')
    grid = [[0 for _ in range(23)] for _ in range(3)]
    for line in f:
        grid.append(list(map(int, line.split())) + [0, 0, 0])
    grid += [[0 for _ in range(23)] for _ in range(3)]
    return grid


def largest_product(grid):
    side = 20
    grid += [0 for _ in range(side + 3)] * 3
    max_product = 0
    for i in range(side):
        for j in range(side):
            for dir_down, dir_right in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
                product = 1
                for k in range(4):
                    try:
                        product *= grid[i + 3 + k * dir_down][j + k * dir_right]
                    except IndexError:
                        print('y = ', i + 3 + k * dir_down)
                        print('x = ', j + k * dir_right)
                        return 'Error'
                    except TypeError:
                        print('y = ', i + 3 + k * dir_down)
                        print('x = ', j + k * dir_right)
                        return 'Error'
                if product > max_product:
                    max_product = product
    return max_product

if __name__ == '__main__':
    outer_grid = read_input()
    print(largest_product(outer_grid))
