# Un palindromo è una parola che si scrive allo stesso
# modo, sia da sinistra -> destra che da destra -> sinistra
# ("noon", "rotator", ecc...)

# Scrivere una Fn che accetta una stringa come argomento e
# ritorna True se questa è una palindromo e False altrimenti

def reverse_word(word):
    return ''.join(reversed(word))


def is_palindrome(word_1):
    """Controllo se una parola è un palindromo

    is_palindrome('bob')
    True
    >>> is_palindrome('alice')
    False
    >>> is_palindrome('a')
    True
    >>> is_palindrome('')
    True
    """
    # print(word_1)
    # print(reverse_word(word_1))
    return word_1 == reverse_word(word_1)


for word in open('../ch_08_string_and_regular_expression/words.txt'):
    if len(word) >= 7 and is_palindrome(word.strip()):
        print(word)
