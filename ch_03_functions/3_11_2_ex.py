# Scrivi una Fn "print_right" che accetta una stringa
# nominata "text" e la stampa in modo che l'ultimo
# carattere si trovi nella 40esima colonna

def print_right(text):
    """Print the text so the last letter is in column 70.

    text: string
    """
    crt = 40 - len(text)
    print(' ' * crt, text)
    # columns = 40
    # space = ' '
    # num_spaces = columns - len(text)
    # print(space * num_spaces + text)


print_right("Alfio")
print_right("Pietrantuono")
