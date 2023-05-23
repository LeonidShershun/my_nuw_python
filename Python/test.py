import re


def balanced(expression):
    count = 0 
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            if count == 0:
                return False
            count -= 1 
    return count == 0

print(balanced(input()))







expression = '(x-{[8*(2*5]}+(2)'
#print(balanced(expression))