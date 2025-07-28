def isvowels(ch):
    return ch.upper() in ['A','E','I','O','U']

def countno(string):
    count = 0 
    for i in string:
        if isvowels(i):
            count += 1
    return count

string = input('Enter a word or a string: ')

print(countno(string))
