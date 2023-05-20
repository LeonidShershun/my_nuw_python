'''Браузер Chrome пропонує нам згенеровані випадкові паролі для сайтів та вебзастосунків. Ми потренуємось розв'язувати подібні завдання.
Розіб'ємо завдання на три етапи. Перший етап — створіть функцію get_random_password, яка буде генерувати випадковий рядок пароля.

Вимоги:

у пароля має бути 8 символів.
для шифрування пароля будемо використовувати наступний набір символів:
()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Ці символи лежать у межах від 40 до 126 коду в таблиці ASCII включно, і доступ до них можна отримати за допомогою функції chr.

chr(40)  # (
chr(126)  # ~
Щоб отримати випадкове ціле значення із заданого діапазону, ми використовуємо стандартний модуль Python random та його функцію randint.
Вона має виклик виду randint(A, B) і повертає випадкове ціле число N, A ≤ N ≤ B.

from random import randint

random_num = randint(40, 126)
Після виконання коду в змінній random_num буде знаходитися випадкове ціле число від 40 до 126 включно.

Таким чином функція get_random_password має випадковим чином вибрати із запропонованого діапазону 8 символів та повернути згенерований
пароль у вигляді рядка.'''

'''
from random import randint


def get_random_password():
'''

from random import randint

random_password = []
d = []


def get_random_password():
    xer = None
    d = []
    while len(d) <= 7:
        z= chr(randint(40, 126))
        d.append(z)
        random_password = ''.join(d)
    print(len(str(random_password)))
    print(d)
    print(random_password)
    return str(random_password)
get_random_password()