# scrivi una Fn "is_triangle" che accetta 3 numeri interi
# come argomenti e verifica se, con i parametri forniti
# si è in grado di creare un triangolo

# per verificare se si può creare un triangolo
# bisogna vedere se una qualsiasi delle tre lunghezze
# fornite è maggiore della somma degli altri due lati
# non si può creare un triangolo, altrimenti si


def is_triangle(a, b, c):
    if a > (b + c):
        print("no")
    elif b > (a + c):
        print('no')
    elif c > (a + b):
        print('no')
    else:
        print('yes')


is_triangle(4, 4, 4)

is_triangle(1, 2, 3)
is_triangle(4, 5, 6)
is_triangle(6, 2, 3)
