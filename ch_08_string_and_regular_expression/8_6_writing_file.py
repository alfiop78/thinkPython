reader = open('book.txt')

# prima di leggere il libro possiamo rimuovere le
# le sezioni di Informazioni sul libro e le informazioni
# sulla licenza, che sono delimitate dai caratteri ***


# La funzione legge una linea del libro e controllo
# se è una linea 'speciale' (informazioni/licenza)
def is_special_line(line):
    return line.startswith('*** ')


# creo un nuovo file con il solo contenuto del libro
# (tutto il testo racchiuso tra *** START... e *** END...)
# l'apertura in mode = 'w' consente la scrittura
writer = open('book_cleaned.txt', 'w')

# leggo tutte le righe fino a *** START, in questo
# modo, la posizione corrente del cursore nel file
# si trova sulla riga con ***
for line in reader:
    if is_special_line(line):
        # trovata linea con sezioni ***
        # print(line.strip())
        # Trovata riga "speciale" interrompo la lettura e...
        break


# ... continuo la lettura delle righe da dove era rimasta nel precedente for
# quindi da *** START....
for line in reader:
    if is_special_line(line):
        # Trovata riga "speciale" interrompo la lettura e...
        # in questo caso la riga trovata è *** END....
        break
        # ...scrivo nel file book_cleaned.txt partendo da *** START....
        # ... fino alla riga con *** END....
    writer.write(line)


# chiusura dei due file
reader.close()
writer.close()

# controllo del risulato ottenuto
for line in open('book_cleaned.txt'):
    line = line.strip()
    if len(line) > 0:
        print(line)
        # il primo ciclo stampa DRACULA (riga 5)
        # poi _by_ (riga 7)
        # infine Bran Stoker (riga 9)
        # quando la riga termina con Stoker interrompo il ciclo
    if line.endswith('Stoker'):
        break
