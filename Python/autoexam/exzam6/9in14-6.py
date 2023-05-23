'''Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True,
якщо рядки дорівнюють собі, і False — якщо ні.'''

'''
def is_equal_string(utf8_string, utf16_string):
'''

def is_equal_string(utf8_string, utf16_string):
    a = utf8_string
    # print(a)
    b = utf16_string
    print(b)
    if a == b:
        return True
    else:
        return False
    ...



print()
s = "Hello! мама"

utf8 = s.encode()
print(utf8)
utf16 = s.encode('utf-16')
print(utf16)
utf8_string = utf8
utf16_string = utf16

print()
print()
print(is_equal_string(utf8_string, utf16_string))
print()