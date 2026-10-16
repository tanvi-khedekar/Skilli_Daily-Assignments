def sumOfFrequencies(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    counts = freq.values()
    return max(counts) + min(counts)