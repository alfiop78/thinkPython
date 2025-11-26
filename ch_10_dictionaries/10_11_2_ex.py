"""
    Scrivere una versione più concisa di value_counts
    utilizzando il get sui Dict
"""


def value_counts(string):
    counter = {}
    for letter in string:
        # if letter not in counter:
        #     counter[letter] = 1
        # else:
        #     counter[letter] += 1
        # la if qui sopra può essere eliminata e, utilizzando
        # get in questo modo si ottiene un codice più conciso
        counter[letter] = counter.get(letter, 0) + 1
    return counter


counter = value_counts('brontosaurus')
print(counter)

# get restituisce il valore della key indicata nel primo parametro
# il secondo parametro è il default se la key richiesta non è presente
print(counter.get('b', 0))  # 1
print(counter.get('c', 0))  # 0
print(counter.get('o', 0))  # 2
print(counter.get('s', 0))  # 2
