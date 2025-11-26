# Pulisco il file pg43, come fatto nel capitolo 8, per
# eliminare contenuti di informazioni del libro e
# lasciare solo il testo del libro


# La funzione legge una linea del libro e controlla
# se è una linea 'speciale' (informazioni/licenza)
def is_special_line(line):
    return line.strip().startswith('*** ')


def clean_file(input_file, output_file):
    reader = open(input_file, encoding='utf-8')
    writer = open(output_file, 'w')

    # leggo tutte le righe fino a *** START, in questo
    # modo, la posizione corrente del cursore nel file
    # si trova sulla riga con ***
    for line in reader:
        if is_special_line(line):
            # trovata linea con sezioni ***
            # print(line.strip())
            # Trovata riga "speciale" interrompo la lettura e...
            break

    # ... continuo la lettura delle righe da dove era rimasta nel precedente
    # for quindi da *** START....
    for line in reader:
        if is_special_line(line):
            # Trovata riga "speciale" interrompo la lettura e...
            # in questo caso la riga trovata è *** END....
            break
            # ...scrivo nel file book_cleaned.txt partendo da *** START....
            # ... fino alla riga con *** END....
        writer.write(line)

    reader.close()
    writer.close()


filename = 'dr_jekyll.txt'

clean_file('pg43.txt', filename)
