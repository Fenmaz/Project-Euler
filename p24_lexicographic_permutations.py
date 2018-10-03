def factorials_list(n):
    if n == 0:
        return [1]
    else:
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[-1]*i)
    return factorials


def lex_permutations(n):
    """
    Find the nth permutation of the basic 10 digits in lexicographic order
    """
    fatorials = factorials_list(10)
    permu = ""
    for i in fatorials[::-1]:
        num = n // i

if __name__ == '__main__':
    print(factorials_list(10))
