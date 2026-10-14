import string

def longestWord(sentence: str) -> str:
    longest = ""
    for word in sentence.split():
        cleaned = word.strip(string.punctuation)
        if len(cleaned) > len(longest):
            longest = cleaned
    return longest