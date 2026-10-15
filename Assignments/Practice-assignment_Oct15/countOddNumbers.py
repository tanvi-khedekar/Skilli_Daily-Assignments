def countOddNumbers(n, array):
    count = 0
    for num in array:
        if num % 2 != 0:
            count += 1
    return count