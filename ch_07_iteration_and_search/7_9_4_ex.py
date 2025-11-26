# uses_all
# Fn che accetta una parola e una stringa di lettere come argomenti
# Verifica se la parola utilizza TUTTE le lettere almeno una volta

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required:
        if letter not in word:
            return False

    return True


print(uses_all("alfio", "fia"))  # True
print(uses_all("banana", "ban"))  # True
print(uses_all("apple", "api"))  # False
