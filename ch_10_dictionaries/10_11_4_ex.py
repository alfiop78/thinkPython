"""
    La funzione find_repeat mappa un dict e restituisce una lista
    di key presenti nel dict più di una volta
"""


def find_repeats(counter):
    """Makes a list of keys with values greater than 1.
    counter: dictionary that maps from keys to counts
    returns: list of keys
    """
    repeats = []
    for key, count in counter.items():
        if count > 1:
            repeats.append(key)

    return repeats


def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


# per svolgere l'esercizio è necessaria anche la fn value_counts
# che restituisce un dict
counter = value_counts('brontosaurus')
print('value_counts', counter)
# ... quindi il counter (che è un dict) lo passo a find_repeats()

print('find_repeat', find_repeats(counter))
# restituisce ['r', 'o', 's', 'u'] perchè sono presenti più
# di una volta nella parola 'brontosaurus'

# esempio con una lista di numeri
counter = value_counts([1, 2, 3, 2, 1])
repeats = find_repeats(counter)
print(repeats)
