def isSubsequence(s,t):
    q = 0
    p = 0

    result = []
    while q < len(t):
        if p < len(s) and t[q] == s[p]:            #p =s,q=t
            result.append(t[q])
            q+=1
            p+=1
        else:
            q+=1
    if result == list(s):
        return True
    return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))