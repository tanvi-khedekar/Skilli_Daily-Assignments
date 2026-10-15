def isPerfectNumber(n: int) -> bool:
    if n <= 1:
        return False

    divisor_sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            if i * i != n:
                divisor_sum += n // i
        i += 1

    return divisor_sum == n