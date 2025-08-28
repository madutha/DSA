# def roman_to_integer(s):
    
#     dict = {"I" : 1,
#             "V" : 5,
#             "X" : 10,
#             "L" : 50,
#             "C" : 100,
#             "D" : 500,
#             "M" : 1000,}
#     total = 0
#     prev_value = 0
#     for char in reversed(s):
#         value = dict[char]
#         if value < prev_value:
            
def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

# Example usage:
print(roman_to_int("MCMXCIV"))  # Output: 1994

            

      
     