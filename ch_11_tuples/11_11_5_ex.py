"""
    Creare un programma che prende una lista di parole e
    restituisce un dict che mappa tutte le parole che sono
    anagrammi della parola passata come parametro
    # stampa tutti i set (insiemi) di parole che sono anagrammi (9_15_2_ex.py)
    es.:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']
"""

word_list = open("words.txt").read().split()


def sort_word(word):
    return ''.join(sorted(word))


anagram_dict = {}
for word in word_list:
    key = sort_word(word)
    if key not in anagram_dict:
        anagram_dict[key] = [word]
    else:
        anagram_dict[key].append(word)

# print(anagram_dict)
# es.: 'fhlortuw': ['worthful', 'wrothful']


def value_length(pair):
    """
        La fn trova l'elenco più lungo di anagrammi (contenuto
        nell dizionario)
        Accetta una coppia key-value dove la key è una stringa
        e il valore è una lista di parole (list), restituisce
        la lunghezza dell'elenco
    """
    key, value = pair

    # pair contiene una Tupla (che deriva da anagram_dict.items())
    # es.: ('aestw', ['sweat', 'tawse', 'twaes', 'waste'])
    # if len(value) > 4:
    #     print(pair)
    #     anagram_dict.items()

    return len(value)


"""
    Possiamo usare questa funzione come chiave di ordinamento
    per trovare gli elenchi più lunghi di anagrammi.
"""
# print('Metodo item() su dict()', anagram_dict.items())
# ordino il dizionario in ordine crescente, gli ultimi elementi
# sono le parole che hanno più anagrammi, anagram_items è una List
anagram_items = sorted(anagram_dict.items(), key=value_length)
print(type(anagram_items))
print("\nVisualizzo le ultime n parole che hanno più anagrammi\n")
for key, value in anagram_items[-5:]:
    print(key, value)


"""
    Se vuoi sapere quali sono le parole più lunghe che hanno
    anagrammi, puoi usare il seguente ciclo per stamparne alcune.
"""
longest = 7
print("\nLe parole più lunghe che hanno anagrammi\n")

for key, value in anagram_items:
    if len(value) > 1:
        word_len = len(value[0])
        if word_len > longest:
            longest = word_len
            print(key, value)
