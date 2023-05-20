'''Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. Функція виконує пошук
зазначеного слова word у тексті text за допомогою функції search та повертає словник.

При виклику функції:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
    and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming
    language, and first released it in 1991 as Python 0.9.0.'
}
де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію
Якщо збігів не виявлено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
    and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming
    language, and first released it in 1991 as Python 0.9.0.'
}
'''

'''import re


def find_word(text, word):
'''

import re


def find_word(text, word):
    final= {}
    final['result'] = None
    final['first_index'] = None
    final['last_index'] = None
    final['search_string'] = word
    final['string'] = text
    if word in text:
        final['result'] = True
        age = re.search(word, text)
        first = age.span()
        final['first_index'] = first[0]
        final['last_index'] = first[1]
        final['search_string'] = word
        final['string'] = text
    else:
        final['result'] = False
        
    
    return final
a = 'Якщо говорити менш формально, то поле заміни може починатися з field_name, яке визначає об’єкт, значення якого має бути відформатовано та вставлено у вихідні дані замість поля заміни. За field_name необов’язково йде поле conversion, якому передує знак оклику'
b = "вихідні дані замість поля заміни"
print(find_word(a, b))