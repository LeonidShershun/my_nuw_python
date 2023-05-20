'''Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних
символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
'''

'''
def real_len(text):
'''

text = 'Al\nKdfe23\t\v.\r'
tt=0

start_len = len(text)
def real_len(text):
    cor = ("\n", "\f", "\t", "\v", "\r")
    for i in cor:
        text = text.replace(i,"")
    global tt
    tt = len(text)
    print(len(text))
    return tt

real_len(text)
print(start_len, tt)