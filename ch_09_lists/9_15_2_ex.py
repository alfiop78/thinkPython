def is_anagram(word1, word2):
    """Controllo se una parola è un'anagramma dell'altra

    >>> is_anagram('tops', 'stop')
    True
    >>> is_anagram('skate', 'takes')
    True
    >>> is_anagram('tops', 'takes')
    False
    >>> is_anagram('skate', 'stop')
    False
    """
    return sorted(word1) == sorted(word2)


for word in open('../ch_08_string_and_regular_expression/words.txt'):
    # print(word)
    if is_anagram(word.strip(), 'takes'):
        print(word)
