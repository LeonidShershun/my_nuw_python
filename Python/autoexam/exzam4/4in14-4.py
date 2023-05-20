'''Сучасна система оцінок в університеті має такий вигляд:
Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, 
get_grade приймає ключ у вигляді оцінки ECTS, і має повертати відповідну п'ятибальну оцінку (перший стовпчик таблиці). 
Друга get_description теж приймає ключ у вигляді оцінки ECTS, але повертатиме пояснення оцінки в текстовому форматі 
(останній стовпчик таблиці) і буде використана в електронній заліковій книжці студента. 
На відсутній ключ функції повинні повертати значення None .'''

'''
def get_grade(key):
    
    


def get_description(key):
'''

def get_grade(key):
    if key == 'F':
        ball = 1
        return ball
    elif key == 'FX':
        ball = 2
        return ball
    elif key == 'E' or key == 'D':
        ball = 3
        return ball
    elif key == 'C':
        ball = 4
        return ball
    elif key == 'B' or key == 'A':
        ball = 5
        return ball
    else:
        return None
def get_description(key):
    if key == 'F' or key == 'FX':
        ball = 'Unsatisfactorily'
        return ball
    elif key == 'E':
        ball = 'Enough'
        return ball
    elif key == 'D':
        ball = 'Satisfactorily'
        return ball
    elif key == 'C':
        ball = 'Good'
        return ball
    elif key == 'B':
        ball = 'Very good'
        return ball
    elif key == 'A':
        ball = 'Perfectly'
        return ball
    else:
        return None

print(get_grade('A')) # == 5
print(get_description('B')) # == Very good