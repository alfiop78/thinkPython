def triangle(text, ripetition):
    """Make a triangle shape by printing a string repeatedly.

    string: characters to be repeated
    height: number of lines in the triangle
    """
    for i in range(ripetition + 1):
        print(text * i)


triangle("L", 5)
