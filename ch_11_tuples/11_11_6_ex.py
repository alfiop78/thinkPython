"""
    Scrivi una funzione chiamata word_distance che prenda
    due parole della stessa lunghezza e restituisca
    il numero di posizioni in cui le due parole differiscono
"""


def word_distance(word1, word2):
    """Computes the number of places where two word differ.

    >>> word_distance("hello", "hxllo")
    1
    >>> word_distance("ample", "apply")
    2
    >>> word_distance("kitten", "mutton")
    3
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        print(c1, c2)
        if c1 != c2:
            count += 1

    return count


print(word_distance("hello", "hxllo"))
print(word_distance("alfio", "algiy"))
print(word_distance("ample", "apply"))
print(word_distance("kitten", "mutton"))
