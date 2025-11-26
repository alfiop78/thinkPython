'''
    Scrivere una Fn 'add_counters' che accetta due dict e
    restituisce un nuovo dict che contiene tutte le lettere
    e il numero totale di volte in cui appaino in entrambe le parole
'''


def add_counters(dict_1, dict_2):
    # result conterrà gli elementi di entrambi i dict
    # inizio ad aggiungere gli elementi del primo dict
    result = dict(dict_1)
    # print(result)
    for letter, count in dict_2.items():
        # ciclo gli elementi presenti in dict_2 per aggiungerli e, se
        # sono già presenti, incrementare gli elmeneti presenti nel dict_1
        result[letter] = dict_1.get(letter, 0) + count

    return result


# utilizzo value_counts per restituire un dict
def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


dict_1 = value_counts('alfio')
dict_2 = value_counts('pietrantuono')


result = add_counters(dict_1, dict_2)
print(result)
