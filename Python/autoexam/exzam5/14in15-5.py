'''Завдання буде схоже на попереднє, але тепер у тексті ми шукатимемо номер телефону України
в міжнародному форматі, шаблон якого наступний: +380(67)777-7-777 або +380(67)777-77-77

Напишіть регулярний вираз для функції find_all_phones, яка буде в тексті (параметр text)
знаходити всі телефонні номери за вказаним шаблоном та повертати список отриманих з тексту
збігів.

З метою спрощення приймемо, що:

використовуємо тільки цифри та символи +, (, ) та -
телефонний номер починається із символу +
шаблон телефону символ + потім три цифри 380, символ (, дві цифри, символ ), три цифри,
символ -, одна або дві цифри, символ -, дві чи три цифри 
Довжина шаблону телефонного номера завжди 17 символів
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів
телефонних номерів.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок
регулярних виразів regex101.'''

'''
import re


def find_all_phones(text):
    result = re.findall(r"", text)
    return result
'''

import re


def find_all_phones(text):
    result = re.findall(r"((\+[0-9]{3}\([0-9]{2}\)[0-9]{3}\-)([0-9]{2}\-[0-9]{2}|[0-9]{1}\-[0-9]{3}))", text)
    res = []
    for phone in result:
        res.append(phone[0])
            
    return res




text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'

print(find_all_phones(text))
print(['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78'])
print()