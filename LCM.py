def findLcm(n1, n2):
    a, b = n1, n2
    while b:
        a, b = b, a % b
    gcd = a
    return (n1 * n2) // gcd