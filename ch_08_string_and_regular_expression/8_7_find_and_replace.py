# sostituire il nome "jonathan" con "Thomas" leggendo il
# file book_cleaned.txt creato nell'esercizio 8.6

# conteggio delle righe del file
total = 0
# imposto qui open() in modo da leggere sempre dall'inizio il file
for line in open('book_cleaned.txt'):
    total += 1

print("Totale righe del libro", total)


total = 0
for line in open('book_cleaned.txt'):
    # linee che contengono "Jonathan"
    if "Jonathan" in line:
        total += 1

print("Totale righe che contengono 'Jonathan'", total)

# possono esserci linee che contengono più "Jonathan" e, nell'istruzione
# precedente non vengono contate
# si utilizza count per contare più occorrenze in una riga

total = 0
for line in open('book_cleaned.txt'):
    # linee che contengono "Jonathan"
    total += line.count("Jonathan")

print("Righe che contengono 'Jonathan' con più occorrenze in una riga", total)

writer = open('book_replaced.txt', 'w')
# replica di Jonathan con Thomas

for line in open('book_cleaned.txt'):
    line = line.replace('Jonathan', 'Thomas')
    writer.write(line)
