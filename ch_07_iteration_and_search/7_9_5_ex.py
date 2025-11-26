def uses_all(word, required):
    """Checks whether a word uses all required letters.
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False

    return True


def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """

    for letter in word.lower():
        if letter not in available.lower():
            return False

    return True


def check_word(word, available, required):
    """Check whether a word is acceptable.
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4:
        return False

    if not uses_all(word, required):
        return False

    return uses_only(word, available)


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    n = len(word)
    if n == 4:
        return 1

    if uses_all(word, available):
        return n + 7
    else:
        return n


# gioco disponibile qui con le lettere del giorno
# https://www.google.com/url?q=https%3A%2F%2Fwww.nytimes.com%2Fpuzzles%2Fspelling-bee
available = 'ACDLORT'
required = 'R'

total = 0

file_object = open('../ch_08_string_and_regular_expression/words.txt')
for line in file_object:
    word = line.strip()
    if check_word(word, available, required):
        score = word_score(word, available)
        total = total + score
        print(word, score)

print("Total score", total)
