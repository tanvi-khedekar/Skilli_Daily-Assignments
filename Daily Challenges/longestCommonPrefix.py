def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return ""
    
    # Take the first string as a base to compare against
    prefix = str[0]
    
    for word in str[1:]:
        # Shorten prefix until the current word starts with it
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
                
    return prefix