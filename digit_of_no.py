def digitno(num):
    sum = 0
    # num = 123
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    
    return sum

print(digitno(123))