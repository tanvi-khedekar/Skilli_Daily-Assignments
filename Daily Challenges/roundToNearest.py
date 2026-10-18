def roundToNearest(s: str):
    digits = list(s)
    last_digit = int(digits[-1])

    # If last digit is <= 5, round down
    if last_digit <= 5:
        digits[-1] = '0'
        return int("".join(digits))

    # Otherwise round up
    digits[-1] = '0'
    carry = 1
    i = len(digits) - 2

    while i >= 0 and carry:
        val = int(digits[i]) + carry
        digits[i] = str(val % 10)
        carry = val // 10
        i -= 1

    if carry:
        digits.insert(0, '1')

    return int("".join(digits))