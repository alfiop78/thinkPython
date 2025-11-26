import re
# Espressioni regolari
# testo da cercare
# text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."

text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."

# pattern utilizzato per la ricerca
pattern = "Dracula"

result = re.search(pattern, text)
print("match", result)


# ricerca nel libro
def find_first(pattern):
    for line in open('book_cleaned.txt'):
        res = re.search(pattern, line)
        if res is not None:
            return res


result = find_first('Harker')

# stampo la prima occorrenza trovata
if result is not None:
    print(result.string)

# l'operatore | (pipe) può corrispondere sia all'operatore a sinistra
# che quello a destra
pattern = "Mina|Murray"
result = find_first(pattern)
if result is not None:
    print(result.string)


# restituisce il numero di righe trovate in base al pattern fornito
def count_matches(pattern):
    count = 0
    for line in open('book_cleaned.txt'):
        result = re.search(pattern, line)
        if result is not None:
            count += 1
    return count


print(count_matches('Mina|Murray'))


# Il carattere ^ cerca all'inizio di una stringa
result = find_first('^Dracula')
if result is not None:
    print(result.string)

# Il carattere $ cerca alla fine di una stringa
result = find_first('Harker$')
if result is not None:
    print(result.string)
