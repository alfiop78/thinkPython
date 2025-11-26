# scrivi una Fn "gdc" che restituisce
# il massimo comune divisore tra i due numeri
# forniti

# Il Massimo Comune Divisore (MCD) di due o più numeri è
# il più grande numero intero che divide esattamente
# tutti i numeri dati, senza lasciare resto

def gcd(a, b):
    # se il resto = 0 è stato trovato il massimo comune divisore
    if b == 0:
        return a
    else:
        # richiamo ricorsivamente la Fn gdc
        return gcd(b, a % b)
