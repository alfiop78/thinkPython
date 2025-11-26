import math
# scrivi una funzione che calcola l'ipotenusa
# che restituisce la lunghezza dell'ipotenusa
# di un triangolo rettangolo, data la lunghezza
# degli altri due cateti come argomenti

# radice quadrata della somma dei cateti elevati al quadrato
# (teorema di pitagora)

# sviluppo incrementale

# 1 step
# def hypot(a, b):
#     return 0

# 2 step
# def hypot(a, b):
#     d2 = a**2 + b**2
#     print(d2)
#     return 0


# step 3
# def hypot(a, b):
#     d2 = a**2 + b**2
#     result = math.sqrt(d2)
#     print(result)
#     return 0


# step 4
# def hypot(a, b):
#     d2 = a**2 + b**2
#     result = math.sqrt(d2)
#     return result


# step 6
def hypot(a, b):
    # sqrt : radice quadrata
    # somma dei cateti elevati al quadrato (a**2 e b**2)
    return math.sqrt(a**2 + b**2)


result = hypot(3, 4)
print(result)
# 5.0
