def check_word(word):
    # la parola da cerca deve contenere una 'e'
    if 'e' not in word:
        return False
    # se la terza o la quinta lettere sono 'e' scarto la parola
    if word[2] == 'e' or word[4] == 'e':
        return False
    # se nella parola ci sono i caratteri 'spadclrk' la scarto
    if uses_any(word, 'spadclrk'):
        return False
    # se nessuno dei casi sopra si sono veriticati allora la parola, dal file
    # words.txt viene restituita
    return True


def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False


# TOTEM
def check_word2(word):
    if not check_word(word):
        return False

    # la quarta lettera deve essere diversa da 'e'
    if word[3] == 'e':
        return False

    # l'ultima lettera deve essere 'm'
    if word[4] != 'm':
        return False

    return True


for line in open('words.txt'):
    word = line.strip()
    # la parola deve essere di 5crt e soddisfare le condizioni di check_word
    # per poter essere stampata
    # if len(word) == 5 and check_word(word):
    if len(word) == 5 and check_word2(word):
        print(word)
