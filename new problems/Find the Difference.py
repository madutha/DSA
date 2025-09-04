def findTheDifference(s,t):
    result = 0
    total = s+t
    for ch in total:
        result ^= ord(ch)
    return chr(result)
        

s = "abcd"
t = "abcde"
print(findTheDifference(s,t))