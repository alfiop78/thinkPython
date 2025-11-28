"""
    analisi del testo di un libro
"""

filename = 'dr_jekyll.txt'


# il loop for legge le righe dal file ed esegue lo split
# per dividere le righe in parole. Tiene traccia delle
# parole univoche e le memorizza, come key, in un dizionario

unique_words = {}
for line in open(filename):
    seq = line.split()
    for word in seq:
        unique_words[word] = 1

len(unique_words)

print(len(unique_words))

# ispezionando le circa 6000 parole restituite
# noteremo che qualche parola non è una parola valida
# Ad esempio, se diamo uno sguardo alle parole più lunghe...

# uso l'ordinamento, in base alla lunghezza della parola (key=len)
# e visualizzo solo gli ultimi 5 elementi
print(sorted(unique_words, key=len)[-5:])

# ...segue in 12_2_puntuaction
