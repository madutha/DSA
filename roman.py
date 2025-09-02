
def roman(s):
    dict = {"I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,}
    prev_value = 0
    total = 0
    for char in reversed(s):
        value = dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total


print(roman("LVIII"))

            