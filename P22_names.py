from string import ascii_uppercase


def inp():
    f = open("p022_names.txt", "r")
    line = f.readline()
    words = line.split(",")
    new_words = []
    for word in words:
        new_word = word.replace("\"", "")
        new_word = new_word.replace(" ", "")
        new_words.append(new_word)

    new_words.sort()
    return new_words


def process(words):
    letters = {}
    for i, letter in enumerate(ascii_uppercase):
        letters[letter] = i + 1

    total = 0
    for i, word in enumerate(words):
        word_worth = 0
        for char in word:
            word_worth += letters[char]
        total += (i + 1) * word_worth

    return total


def test(words):
    print(words[937])
    print(process([words[937]]))


if __name__ == '__main__':
    print(process(inp()))
