def reverse_string(s):
    p = 0
    q = len(s)-1
    while p<q:
        s[p],s[q] = s[q],s[p]
        p+=1
        q -=1
    return s
    # stack = []
    # for i in s:
    #     stack.append(i)
    # i = 0
    # while stack:
    #     s[i]= stack.pop()
    #     i+=1
    # return s



s = ["h","e","l","l","o"]
print(reverse_string(s))