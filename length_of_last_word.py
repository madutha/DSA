def length_of_last_word(s):
    # s = s.strip()
    s = s.split()
    reverse_words = s[::-1]
    return len(reverse_words[0])
s = "   fly me   to   the moon  "
print(length_of_last_word(s))