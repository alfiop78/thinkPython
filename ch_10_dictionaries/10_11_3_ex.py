"""
    Creare una funzione chiamata has_duplicate che accetta
    una stringa come parametro e ritorna True se c'è un
    elemento che appare nella lista più di una volta
"""


def has_duplicates(t):
    """Check whether any element in a sequence appears more than once.

    >>> has_duplicates('banana')
    True
    >>> has_duplicates('ambidextrously')
    False
    >>> has_duplicates([1, 2, 2])
    True
    >>> has_duplicates([1, 2, 3])
    False
    """
    d = {}
    for x in t:
        d[x] = True
        # print(d)
    # se len(d) è minore della stringa fornita come parametro
    # ci sono elementi duplicati
    return len(d) < len(t)


# print(has_duplicates('bana'))  # True perchè la 'a' compare più di una volta
#
# print(has_duplicates('alfio'))  # False
#
# print(has_duplicates([1, 2, 3, 4, 4]))  # True


no_repeats = []
reader = open('../ch_08_string_and_regular_expression/words.txt', 'r')
# print(reader)
for word in reader:
    # print(word)
    if len(word) > 12 and not has_duplicates(word):
        # se la parola in ciclo ha più di 12 crt e non ha lettere duplicate
        # viene aggiunta alla list no_repeat
        no_repeats.append(word.strip())


print(no_repeats)
