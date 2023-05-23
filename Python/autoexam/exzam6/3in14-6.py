'''У попередній задачі ми записали співробітників у файл у такому вигляді:

Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19
Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), яка читатиме дані з файлу
та повертатиме список співробітників у вигляді:

['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його необхідно прибирати
при додаванні прочитаного рядка до списку.

Вимоги:

прочитайте вміст файлу за допомогою режиму "r".
ми поки що не використовуємо менеджер контексту with
поверніть із функції список співробітників із файлу
'''

'''
def read_employees_from_file(path):
'''


def read_employees_from_file(path):
    fh = open(path, 'r')
    data = []
    while True:
        data1 = fh.readline()
        if not data1:
            break
        
        data.append(data1)
    result = []
    for i in data:
        result.append(i.replace('\n', ''))
      
    
    
    fh.close()
    return result



path = 'test_for_file2.txt'
print()
print(read_employees_from_file(path))
print()