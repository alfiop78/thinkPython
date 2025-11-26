word_list = open("words.txt").read().split()
# uso il word_list abbreviato per fare le prove
# word_list = [
#     'abatis',
#     'abatises',
#     'abator',
#     'abators',
#     'abattis,'
#     'abattises',
#     'abattoir',
#     'abattoirs',
#     'abaxial',
#     'abaxile',
#     'abbacies',
#     'abbacy',
#     'abbatial',
#     'abbe',
#     'abbes',
#     'abbess',
#     'abbesses',
#     'abbey',
#     'abbeys',
#     'abbot',
#     'abbotcies',
#     'abbotcy',
#     'abbots',
#     'abbreviate'
# ]


# Restituisce una lista di tutte le parole che possono essere
# formate eliminando una lettera
def children(word):
    """Returns a list of all words that can be formed by removing one letter.

    word: string

    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        # il primo ciclo (index = 0) crea 'child' senza la prima
        # lettera, il secondo ciclo (index = 1) senza la
        # seconda lettere e così via...
        # print("index : ", i, "\nword ", word, " child : ", child)
        # verifico se 'child' è una parola vera andando a
        # controllare in word_list
        if child in word_dict:
            res.append(child)

    # print(res)
    return res


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.
It starts with the empty string."""

memo = {}
memo[''] = ['']


def reduce_word(word):
    """If word is reducible, returns a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is
    reducible.  The empty string is also reducible.

    word: string
    """
    # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word):
        if reduce_word(child):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.

    If there is more than one choice, it chooses the first.

    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = reduce_word(word)
    print_trail(t[0])


def all_reducible():
    """Checks all words in the word_dict; returns a list of reducible ones.
    """
    res = []
    for word in word_dict:
        t = reduce_word(word)
        if len(t) > 0:
            res.append(word)
    return res


word_dict = {}
# creazione del dizionaria word_dict, vengono aggiunte
# anche 'a', 'i', '' nel dizionario (non sono presenti
# in word_list)
for word in word_list:
    word_dict[word] = 1

# have to add single letter words to the word list;
# also, the empty string is considered a word.
for word in ['a', 'i', '']:
    word_dict[word] = 1

# find the reducible words and sort by length
words = all_reducible()
sorted_words = sorted(words, key=len)

# print the longest words
for word in sorted_words[-10:]:
    print_trail(word)
    print('')
