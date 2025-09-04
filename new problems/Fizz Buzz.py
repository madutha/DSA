def FizzBuzz(n):
    s = n+1
    result = []
    for i in range(1,s):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

n = 3
print(FizzBuzz(n))