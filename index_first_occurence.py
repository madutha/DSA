def strStr(haystack,needle):
    for i in range(len(haystack)-len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
            
haystack = "hello"
needle = "ll"
print(strStr(haystack,needle))