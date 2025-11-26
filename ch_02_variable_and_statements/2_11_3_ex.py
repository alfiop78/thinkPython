# calcolo del volume di una sfera con raggio 5
import math
# part 1

# raggio in cm
radius = 5
# (1) volume = raggio al cubo 5 * 5 * 5 = 125
# radius = 5**3

# (2) moltiplica 125 * 4 = 500
# (3) 500 * pi.greco  = 1570
# (4) 1570 / 3
# volume = radius * 4 * math.pi / 3 in cm cubici
volume = 4 / 3 * math.pi * radius**3

print(volume)


# part 2
x = 42
# x = coseno di x al quadrato + seno di x al quadrato
# il quadrato in pythom : pow(base, esponente)
# cos = math.pow(math.cos(x), 2)
# sin = math.pow(math.sin(x), 2)
# result = cos + sin
# ...scritta su un unica riga
result = math.pow(math.cos(x), 2) + math.pow(math.sin(x), 2)
print(result)

print(math.e**2)

print(math.pow(math.e, 2))

print(math.exp(2))
