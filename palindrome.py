def palindrome(num):
    sum = 0
    bk = num
    while num!=0:
        remain = num%10
        sum = remain + sum*10
        num = num//10
    return bk == sum

print(palindrome(123454321))
