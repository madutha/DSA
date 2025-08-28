def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    else:
        sum = 0
        bk = x
        while x!=0:
            reverse = x%10
            sum = reverse + sum*10
            x = x//10
        return sum == bk
x= -121
print(isPalindrome(x))



