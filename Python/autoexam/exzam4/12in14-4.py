'''І, нарешті, третій, останній етап. Використовуючи рішення із попередніх двох завдань, напишіть
функцію get_password, яка згенерує нам випадковий надійний пароль та поверне його. Алгоритм простий — ми
генеруємо пароль за допомогою функції get_random_password і, якщо він проходить перевірку на надійність
функцією is_valid_password, повертаємо його, якщо ні — повторюємо ітерацію знову.

Примітка: Хорошою практикою буде обмежити кількість спроб (наприклад, до 100), щоб не отримати
нескінченний цикл.'''

'''
from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
'''

import string
from random import randint, randrange


def get_random_password():
    password = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        password = password + random_symbol
        count = count + 1
    return password


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
    return result



def get_password():
    while True:
        password = (get_random_password())
        too = is_valid_password(password)
        if too == True:
            result1 = password
            return result1
            break
        



result2 = get_password()
print(result2)
