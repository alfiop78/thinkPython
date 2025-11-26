# scrivi una Fn chiamata reverse_sentence che accetta come argomento
# una stringa che contiene qualsiasi numero di parole separate dallo
# spazio.
# Dovrebbe restituire una nuova stringa che contiene le stesse parole
# in ordine inverso.
# "Reverse this sentence" il risultato -> "Sentence this reverse"

def reverse_sentence(sentence):
    '''Reverse the words in a string and capitalize the first.

    >>> reverse_sentence('Reverse this sentence')
    'Sentence this reverse'

    >>> reverse_sentence('Python')
    'Python'

    >>> reverse_sentence('')
    ''

    >>> reverse_sentence('One for all and all for one')
    'One for all and all for one'
    '''
    print(sentence)
    split_word = sentence.split()
    return ' '.join(reversed(split_word)).capitalize()


# reverse_sentence("Prima frase")
print(reverse_sentence("Prima frase"))
print(reverse_sentence("Invertire una frase in python"))
print(reverse_sentence("Python"))
