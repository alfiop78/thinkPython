'''
    creare una Fn 'is_interlocking' che accetta una parola come
    argomento e restituisce True se può essere divisa in due
    parole interconnesse
'''


def is_interlocking(word):
    # restituisce lettere alternate (step : 2) partendo dal primo crt
    first = word[0::2]
    # restituisce lettere alternate (step : 2) partendo dal secondo crt
    second = word[1::2]

    return first in word_dict and second in word_dict


reader = open('../ch_08_string_and_regular_expression/words.txt')
word_dict = dict()
# oppure word_dict = {}

for word in reader:
    word_dict[word.strip()] = 1
    if len(word.strip()) >= 8 and is_interlocking(word.strip()):
        first = word[0::2]
        second = word[1::2]
        print(word, first.strip(), second.strip())
