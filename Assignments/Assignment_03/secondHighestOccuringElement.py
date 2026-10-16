def secondHighestOccurringElement(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    # Get all distinct frequencies sorted from highest to lowest
    counts = sorted(set(freq.values()), reverse=True)

    # If there is no second highest frequency, return -1[cite: 15]
    if len(counts) < 2:
        return -1

    second_freq = counts[1]

    # Find the smallest number that has the second highest frequency[cite: 15]
    ans = float("inf")
    for x in freq:
        if freq[x] == second_freq:
            ans = min(ans, x)

    return ans