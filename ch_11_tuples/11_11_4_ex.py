"""
    Crea una fn most_frequent_letters che accetta una stringa
    e stampa le lettere in ordine descrescente di frequenza
"""


def most_frequent_letters(text):
    counter = value_counts(text)
    print(counter)
    # con items() viene creata una lista di tuple, per poterla ordinare
    print(counter.items())
    # il secondo parametro, key (che richiama una fn) consente di ordinare
    # per il secondo elemento della tupla, quindi il numero della frequenza
    # ... reverse=True in ordine desscrescente
    pairs = sorted(counter.items(), key=second_element, reverse=True)
    for key, value in pairs:
        print(key, value)


def second_element(t):
    return t[1]


def value_counts(string):
    """
        Restituisce un dict con le lettere più frequenti in una
        stringa
    """
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


most_frequent_letters('rtgseekjfff')
