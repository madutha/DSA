def plusone(digits):
    converted = []
    value = 0
    for i in digits:
        value = value*10 + i 
    for i in str(value +1):
        converted.append(int(i))
    return converted


    



        


digits = [1,2,3]
print(plusone(digits))
