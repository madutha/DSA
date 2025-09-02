def reverseVowels(self, s: str) -> str:
    ch = list(s)
    p = 0
    q = len(s)-1
    vowels = {
    "a": "a", "e": "e", "i": "i", "o": "o", "u": "u",
    "A": "A", "E": "E", "I": "I", "O": "O", "U": "U"
    }

    while p<q:
        if ch[p] in vowels and ch[q] in vowels:
            ch[p],ch[q] = ch[q],ch[p]
            p+=1
            q-=1
        elif ch[p] in vowels and ch[q] not in vowels:
            q-=1
        elif ch[p] not in vowels and ch[q] in vowels: 
            p+=1
        elif ch[p] not in vowels and ch[q] not in vowels: 
            p+=1
            q-=1
    return "".join(ch)

s = "IceCreAm"
print(reverseVowels(s))