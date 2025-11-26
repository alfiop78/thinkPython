# import os
import re

# vedere come si utilizzano i comandi del so, questo funziona solo con jupyter
# if not os.path.exists('pg1184.txt'):
#     !wget "https://www.gutenberg.org/cache/epub/1184/pg1184.txt"


# contare il numero di righe che contengono un insieme di parola
# pattern = '(pale|pales|paled|paleness|pallor)'

# il pattern con l'utilizzo di \b bounduary esclude 'impale' ad esempio
# la r prima del pattern indica che è una stringa raw (grezza) ed
# è necessaria perchè il pattern contiene caratteri di escape
pattern = r'\b(pale|pales|paled|paleness|pallor)\b'


# restituisce il numero di righe trovate in base al pattern fornito
def count_matches(pattern):
    count = 0
    for line in open('pg1184.txt'):
        result = re.search(pattern, line)
        if result is not None:
            # print(line)
            count += 1
    return count


print(count_matches(pattern))
