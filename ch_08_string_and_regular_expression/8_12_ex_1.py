"""
    emulazione del comando head.
    Scrivere una Fn che accetta come argomento il nome di
    un file da leggere, il numero di righe da leggere e il
    nome del file su cui scrivere le linee lette.
    Se il terzo parametro e None visualizzo le righe lette
    anzichè scriverle nel file
"""


def head(input_file, line_number=10, output_file=None):
    reader = open(input_file, 'r')
    writer = None

    if output_file is not None:
        writer = open(output_file, 'w')

    for i in range(line_number):
        line = reader.readline()
        if output_file is not None and writer is not None:
            writer.write(line)
        else:
            print(line, end='')

    reader.close()
    if output_file is not None and writer is not None:
        writer.close()


head('book_cleaned.txt', 50, 'head.txt')
# head('book_cleaned.txt', 50)
