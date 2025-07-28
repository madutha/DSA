def perfect_square(str):
    num = int(str**0.5)
    flo = str**0.5
    return num == flo

str = 16

print(perfect_square(str))