"""
    Scrivere una fn shift_word che accetta come parametri
    una string e un intero e restituisce una nuova stringa
    che contiene le lettere della stringa spostata del numero
    di posizioni specificato
"""

letters = 'abcdefghijklmnopqrstuvwxyz'
# crea un range di numeri da 0 a 25
numbers = range(len(letters))
# creo un dictionary che mappa ogni lettera al suo indice
letter_map = dict(zip(letters, numbers))

# lettera e
# print(letters[4])

# accesso alla lettera 'a' tramite il suo indice
# print(letter_map['b'])


def shift_word(word, n):
    """Shift the letters of `word` by `n` places.

    >>> shift_word('cheer', 7)
    'jolly'
    >>> shift_word('melon', 16)
    'cubed'
    """
    shifted = []
    for letter in word:
        # index della lettere con l'aggiunta dello shift di 'n' posizioni
        # con il modulo (% 26) index conterrà il resto della divisione
        # quindi, 24 % 26 restituisce 2 in modo da prendere la terza
        # lettera di letters
        index = (letter_map[letter] + n) % 26
        shifted.append(letters[index])
        # print(shifted)

    return ''.join(shifted)


# jolly
print(shift_word('cheer', 7))
# cubed
print(shift_word('melon', 16))
