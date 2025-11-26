# uses_only
# Funzione che accetta una parola e una stringa di lettere
# restituisce True se la parola contiene solo lettere nella
# stringa disponibili nel parametro "available"

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """

    for letter in word:
        if letter not in available:
            return False

    return True


# False, "alfio" usa anche le lettere "a", "l", "o"
print(uses_only('alfio', 'fi'))
# True perchè usa solo le lettere "b", "a", "n"
print(uses_only('banana', 'ban'))
print(uses_only('apple', 'apl'))
