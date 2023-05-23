'''Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

Приклад файлу:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл і
повертати загальну суму заробітної плати всіх розробників компанії.

Вимоги до завдання:

функція total_salary повертає значення типу float
для читання файлу функція total_salary використовує лише метод readline
ми поки що не використовуємо менеджер контексту with'''

'''
def total_salary(path):
'''

import re

def total_salary(path):
    fh = open(path, 'r')
    result = 0.00
    while True:
        line = fh.readline()
        if not line:
            break
        iterator = re.finditer(r"[0-9.]{1,}", line)
        for match in iterator:
            result += float(match.group())
    fh.close()   
    return result
    

    
path = 'test_for_file.txt'
print()
print(total_salary(path))

print()