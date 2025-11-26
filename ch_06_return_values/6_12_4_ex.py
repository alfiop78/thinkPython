# funzione di Ackermann

def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


result = ackermann(3, 2)

print(result)
# 29

result = ackermann(3, 3)
print(result)
# 61

result = ackermann(3, 4)
print(result)
# 125
