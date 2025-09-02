def anagram(s,t):
    sort_s = sorted(s)
    sort_t = sorted(t)
    for i in range(len(s)):
        if sort_s[i] == sort_t[i]:
            continue
        else:
            return False
    return True


   






s = "anagram"
t = "nagaram"    
print(anagram(s,t))
