# scrivi una Fn chiamata "total_length" che accetta una lista di
# stringhe e restituisce la lunghezza totale delle stringhe
# La lunghezza totale delle parole (words.txt) dovrebbe essere
# 902.728

def total_length(string_list):
    total = 0
    for string in string_list.split():
        total += len(string)
    return total


# read legge l'intero file in una stringa
reader = open('../ch_08_string_and_regular_expression/words.txt').read()

print(total_length(reader))

# 902728
