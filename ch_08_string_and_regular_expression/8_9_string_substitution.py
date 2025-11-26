import re
# string substitution


# cerco una sequenza che inizia con 'cent' e può
# finire sia con 'er' che con 're'
pattern = 'cent(er|re)'


# ricerca nel libro
def find_first(pattern):
    for line in open('book_cleaned.txt'):
        res = re.search(pattern, line)
        if res is not None:
            return res


result = find_first(pattern)

# stampo la prima occorrenza trovata
if result is not None:
    print(result.string)


# il carattere '?' indica che il carattere in quella posizione è facoltativo
pattern = 'colou?r'
result = find_first(pattern)

# stampo la prima occorrenza trovata
if result is not None:
    print(result.string)
    line = result.string
    # sostituzione di stringa con sub
    sub = re.sub(pattern, 'color', line)

    # effettuata sostituzione 'colored' al posto di 'coloured'
    print("sub", sub)
