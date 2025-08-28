def palindrome(s):
    
    result1 = []
    result2 = []
    
    s = s.lower()
    
    for i in range(len(s)):
        if s[i].isalpha()== True:
            result1.append(s[i])
    
    for j in range(len(result1)-1,-1,-1):
        result2.append(result1[j])

    for k in range(len(result1)-1):
        if result1[k] != result2[k]:
            return False
    return True
    



def isPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        while left<right and not s[left].isalnum():
            left+=1
        while left < right and not s[right].isalnum():
            right-=1
        if s[left].lower() != s[right].lower():
            return False
        left+=1
        right-=1
    return True

s = "madam"

print(isPalindrome(s))