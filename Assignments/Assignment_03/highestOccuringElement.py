def highestOccurringElement(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    max_count = 0
    ans = float("inf")

    for x in freq:
        if freq[x] > max_count:
            max_count = freq[x]
            ans = x
        elif freq[x] == max_count:
            ans = min(ans, x)

    return ans