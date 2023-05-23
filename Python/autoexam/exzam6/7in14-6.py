'''РОБОТА З ДВОМА ФАЙЛАМИ
Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу
source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write
'''

'''
def sanitize_file(source, output):
'''

import re
def sanitize_file(source, output):
    sec = str()
    with open(source, 'r') as fh:
        while True:
            data = fh.readline()
            data1 = re.finditer("[^0-9]{1,}", data)
            for match in data1:
                sec += str(match.group())
                print(sec)
            if not data:
                break 
    with open(output, 'w') as fh:
         fh.write(sec)   




    return sec  



source = 'test_for_file6.txt' 
output = 'test_for_file7.txt'
print()
#sanitize_file(source, output)
print(sanitize_file(source, output))
print()
#print({'id': '60b90c3b13067a15887e1ae4', 'name': 'Watermelon Cucumber Salad', 'ingredients': ['1 large seedless watermelon', '12 leaves fresh mint', '1 cup crumbled feta cheese']})
print()