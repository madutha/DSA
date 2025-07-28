def armstrong(num):
    sum = 0
    bk = num
    while num !=0:
        rem = num % 10
        sum = sum + rem**3
        num = num // 10
    return sum == bk

print(armstrong(153))