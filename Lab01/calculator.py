def sum(m, n):
    while n > 0:
        n -= 1
        m += 1
    while n < 0:
        n += 1
        m -= 1
    return m

def divide(m, n):
    if n == 0:
        raise ZeroDivisionError
    k = 0
    s = -1 if (m < 0) != (n < 0) else 1
    m, n = abs(m), abs(n)
    while m >= n:
        m -= n
        k += 1
    return k*s
