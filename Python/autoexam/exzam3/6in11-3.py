'''Створіть функцію format_string для форматування рядка. У функцію ми передаємо рядок string та length довжину нового рядка.
Функція повертає новий рядок за наступним алгоритмом:

Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.
Тести на правильність роботи функції виконуються для наступних наборів аргументів:

string='aaaaaaaaaaaaaaaaac', length=12
length=15, string='abaa' '''

'''
def format_string(string, length):
'''

def format_string(string, length):
    if len(string) >= length:
        return (string)
    else:
        koef = (length - len(string)) // 2
        new_string = ' ' * koef + string
        return (new_string)