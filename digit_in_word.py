def digit_in_word(num):
    dict = {
        1 : "One",
        2 : "Two",
        3 : "Three",
        4 : "Four",
        5 : "Five",
        6 : "Six",
        7 : "Seven",
        8 : "Eight",
        9 : "Nine",
        0 : "Zero" 
    }
    ans = ""
    num = str(num)
    for i in num:
        val = dict[int(i)]
        ans = ans + (val + " " if i != str(len(num)) else val)
    return ans

print(digit_in_word(1234))

