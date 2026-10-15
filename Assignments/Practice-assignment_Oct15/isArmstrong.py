def isArmstrong(n: int) -> bool:
    s = str(n)
    num_digits = len(s)
    total = sum(int(digit) ** num_digits for digit in s)
    return total == n