# uses_none
# scrivi una Fn che accetta una parola e una stringa di
# lettere "proibite" e restituisce True se la parola
# non usa nessuna delle lettere proibite


def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in word:
        if letter in forbidden:
            return False

    return True


result = uses_none('alfio', 'prtkm')
print(result)
# False

result = uses_none('alfio', 'prfkm')
print(result)
# True
