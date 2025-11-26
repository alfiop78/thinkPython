# Utilizzo della divisione e dell'operatore "resto" per
# calcolare il tempo dall epoch time in giorni, ore,minuti e secondi
from time import time

now = time()

print(now)

# giorni

seconds_per_day = 24 * 60 * 60
days = now // seconds_per_day
print(days)

# ore

remainder = now % seconds_per_day
hours = remainder // 3600
print(hours)

# minuti

remainder = remainder % 3600
minutes = remainder // 60
print(minutes)

# secondi

seconds = remainder % 60
print(seconds)
