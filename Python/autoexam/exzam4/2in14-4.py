'''При аналізі даних часто виникає необхідність позбавитися екстремальних значень, перш ніж почати 
працювати з даними далі. Напишіть функцію prepare_data, яка видаляє з переданого списку найбільше 
та найменше значення, сортує його в порядку зростання і повертає змінений список як результат.'''

'''
def prepare_data(data):
'''

def prepare_data(data):
    print(data)
    new_data = sorted(data)
    z = len(new_data)
    print(z)
    new_data.pop(0)
    new_data.pop(z-2)
    print(new_data)
    return new_data