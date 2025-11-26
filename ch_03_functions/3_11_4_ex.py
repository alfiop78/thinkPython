def rectangle(text, width, height):
    """Make a rectangle by printing a string repeatedly.

    string: characters to be repeated
    width: number of repetitions on each line
    height: number of lines
    """
    for i in range(height):
        print(text * width)


rectangle("H", 5, 4)
