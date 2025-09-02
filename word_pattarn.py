def word_pattern(pattern, s):
    word = s.split(" ")

    char = {}
    word = {}
    if len(pattern) != len(word):
        return False
    for c,w in zip(pattern,word):
        if c in char and char[c] != w:
            return False
        if w in word and word[w] != c:
            return False
        char[c] = w
        word[w] = c
    return True

    









pattern = "abb"
s = "dog cat cat dog"
print(word_pattern(pattern,s))