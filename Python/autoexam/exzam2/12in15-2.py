'''Повернемося знову до нашого попереднього завдання.

Напишіть два подвійні цикли. У першому циклі while ми постійно запитуємо ціле число, а у другому
за допомогою циклу for обчислюємо суму парних чисел від 0 до введеного числа. Вихід з першого циклу здійснюємо,
якщо ввели число 0 за допомогою оператора break.

Тести використовують дві тестові послідовності чисел:

10, 13, 73, 0 і чекають на суму 1404
1, 2, 3, 4, 0 і чекають на суму 10'''


'''
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if
            
        sum = sum + i
'''

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2 != 0:
            continue
        else:
            sum = sum + i