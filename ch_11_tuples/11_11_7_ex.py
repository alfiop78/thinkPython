"""
    La "metatesi" è la trasposizione di lettere in una parola.
    Due parole formano una "coppia di metatesi" se è possibile
    trasformarne una nell'altra scambiando due lettere, come
    "converse" e "conserve". Scrivi un programma che trovi
    tutte le coppie di metatesi nell'elenco di parole.

    Suggerimento: le parole in una coppia di metatesi devono
    essere anagrammi l'una dell'altra.
"""

word_list = open("words.txt").read().split()


def sort_word(word):
    return ''.join(sorted(word))


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
        # print(c1, c2)
        if c1 != c2:
            count += 1

    return count


# creo e popolo un dict di anagrammi
anagram_dict = {}
for word in word_list:
    key = sort_word(word)
    if key not in anagram_dict:
        anagram_dict[key] = [word]
    else:
        anagram_dict[key].append(word)


# es. anagram_dict= 'fhlortuw': ['worthful', 'wrothful']
for anagrams in anagram_dict.values():
    # con values() recupero la list, quindi : ['worthful', 'wrothful']
    for word1 in anagrams:
        for word2 in anagrams:
            # print('words', word1, word2, word1 < word2)
            # word_distance restituisce il numero di posizioni che sono
            # scambiate (vedere 11_11_6_ex.py)
            if (len(word1) >= 10 and word1 < word2
                    and word_distance(word1, word2) == 2):
                print(word1, word2)
