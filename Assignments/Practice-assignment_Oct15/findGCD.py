def gcdOfTwoNumbers(n1: int, n2: int) -> int:
    while n2:
        n1, n2 = n2, n1 % n2
    return n1