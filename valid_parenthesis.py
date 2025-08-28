# def isValid(s):
#     dict = {')': '(', '}': '{', ']':'['}
#     stack = []

#     opening_brackets = set(["(","{","["])
    
    
#     for i in s:
#         if i in opening_brackets:
#             stack.append(i)
#         elif stack and stack[-1] == dict[i]:
#             stack.pop()
#         else:
#             False

#     if stack:
#         return False
#     else:
#         return True

    
    


# s = "([])"

# print(isValid(s))
    
def isvalid(s):
    dict = {
        ")":"(",
        "}":"{",
        "]":"["
            }
    stack = []
    closeing = [")","}","]"]
    if s[0] in closeing:
        return False
    else:
        for i in s:
            if i in dict.values():
                stack.append(i)
            elif len(stack) != 0 and stack[-1] == dict[i]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True



s = "(])"

print(isvalid(s))