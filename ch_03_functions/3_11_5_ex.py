
def bottle_line(n, suffix):
    """Display a line from 99 Bottles of Beer.

    n: integer
    suffix: string
    """
    print(n, 'bottles of beer', suffix)


def bottle_verse(n):
    """Display a verse from 99 Bottles of Beer.

    n: integer
    """
    bottle_line(n, 'on the wall')
    bottle_line(n, '')
    print('Take one down, pass it around')
    bottle_line(n-1, 'on the wall')


for n in range(89, 0, -1):
    bottle_verse(n)
    print()
