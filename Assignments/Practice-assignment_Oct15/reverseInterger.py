def reverseInteger(n):
    isNeg = False
    if n < 0:
        isNeg = True
        n = -n
        
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        
    if isNeg:
        rev = -rev

    return rev