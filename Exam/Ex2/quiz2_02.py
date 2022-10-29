def match(word, pattern, include_chars, exclude_chars):
    if len(word) != len(pattern): return False
    for i in range(len(word)):
        if word[i] != pattern[i] and pattern[i] != "?":
            return False
    for i in range(len(word)):
        if pattern[i] == "?" and word[i] in exclude_chars:
            return False
    for ic in include_chars:
        rep = False
        newPattern = pattern
        for i in range(len(word)):
            if pattern[i] == "?" and word[i] == ic:
                rep = True
                newPattern = pattern[: i] + word[i] + pattern[i+1: ]
        pattern = newPattern
        if not rep: return False

    # print("Should return True")
    return True

exec(input()) # DON'T remove this line
# print(exec(input())) # DON'T remove this line
