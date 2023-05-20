'''Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр
— пароль на надійність.

Критерії надійного пароля:

1 Довжина рядка пароля вісім символів.
2 Містить хоча б одну літеру у верхньому регістрі.
3 Містить хоча б одну літеру у нижньому регістрі.
4 Містить хоча б одну цифру.

Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на
надійність. Інакше повернути False.'''

'''
def is_valid_password(password):
'''

import string
from random import randint, randrange

def is_valid_password(password):
    upper = 0
    lower = 0
    numer = 0
    ap = string.ascii_uppercase
    br = string.ascii_lowercase
    co = string.digits
    result = None
    for i in password:
        t = ap.count(i)
        upper += t
        t1 = br.count(i)
        lower += t1
        t2 = co.count(i)
        numer += t2
        if upper >=1 and lower >=1 and numer >=1 and len(password) == 8:
            result = True
        else:
            result = False 
    #print(result)                    
    return result

password = 'NmlDl1V0'
print(is_valid_password(password))