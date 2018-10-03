from num2words import num2words


def count_letters(n):
    sum_letter = 0
    for i in range(1, n + 1):
        word = num2words(i)
        word = word.replace(" ", "")
        word = word.replace("-", "")
        word = word.replace(",", "")
        sum_letter += len(word)
    return sum_letter

if __name__ == '__main__':
    print(count_letters(1000))
