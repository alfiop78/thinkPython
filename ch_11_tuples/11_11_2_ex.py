# aggiungere un elemento alla tupla
list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(t)

# aggiungo 6 alla fine della seconda tupla
t[1].append(6)
print(t)
print(type(t))

# genera un errore perchè le tuple non sono modificabili
# d = {t: 'stringa di esempio'}

# print(d)
