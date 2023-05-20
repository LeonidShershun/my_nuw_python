'''Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції find_all_emails,
яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих з тексту збігів.

З метою спрощення приймемо, що:

ми використовуємо для email, — англійський алфавіт
префікс (все, що знаходиться до символу @) починається з латинської літери та може містити будь-яке число або
букву, включаючи нижнє підкреслення та символ точки. Має складатися мінімум із двох символів
суфікс email (все, що знаходиться після символу @) складається лише з букв англійського алфавіту, та має дві
частини, розділені точкою, також доменне ім'я верхнього рівня не може бути менш ніж два символи
(все, що після точки)
Даний регулярний вираз жодною мірою не претендує на покриття всіх можливих варіантів email.

При виконанні цього завдання ми рекомендуємо використовувати наступний сервіс для перевірок 
регулярних виразів regex101.'''

'''
import re


def find_all_emails(text):
    result = re.findall(r"", text)
    return result
'''

import re


def find_all_emails(text):
    
    rest = re.findall(r"\b[a-zA-Z0-9._]{2,}@[a-z]+\.[a-z]{2,}", text)
    res = []
    for mail in rest:
        if mail[0] == 1 or mail[0] == '1':
            a = '1'
            mail = re.sub(a, '', mail, count=1)
            
            res.append(mail)
        elif 48 <= ord(mail[0]) <= 57 and 48 <= ord(mail[1]) <= 57 and 48 <= ord(mail[2]) <= 57 and 48 <= ord(mail[3]) <= 57 and 48 <= ord(mail[4]) <= 57 and 48 <= ord(mail[5]) <= 57:
            print(mail)
            continue
        else:
            res.append(mail)
            
    return res

#text = '1Fool@iana.org 222111@test.com'
#text = 'cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'
text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org 222111@test.com'
#text = 'Hi. My fgg65_bg@gyy.gh name`s Valentina leonidshershun@gmail.com and I`m from Ukraine. I very fond of English g@fr.hr lessons. I study at moremuh@fgh.go English School Success Language center. It`s not a very big school. But it`s not very little school. Classes teach Helena Anatolievna. I love English teacher so much. She`s the best! We have English lessons once a week. I`m good at English, Pierre, but my favorite lesson is Math too. What class do you like?'
print(find_all_emails(text))
print()
#print(['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com'])
#print(['cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com']) #['cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com']