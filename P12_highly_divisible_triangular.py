from ProjectEuler.num_handle import find_divisor


def divisible_triangular(n):
    triangular = [1, 3]
    divs = [1, 2, 2]
    k = 2
    num_div = 2
    while num_div < n:
        k += 1
        triangular.append(k * (k+1) // 2)
        divs.append(find_divisor(k + 1))
        if k % 2 == 0:
            num_div = divs[(k // 2) - 1] * divs[k]
        else:
            num_div = divs[(k - 1) // 2] * divs[k - 1]
    return triangular[-1]

if __name__ == '__main__':
    print(divisible_triangular(500))
