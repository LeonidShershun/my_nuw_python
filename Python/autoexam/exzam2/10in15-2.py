'''Напишіть два цикли, вкладені один в один. У першому циклі while ми постійно запитуємо ціле число, а у другому з
допомогою циклу for складаємо суму чисел від 0 до введеного числа включно і додаємо до змінної sum. Змінна sum накопичує суми,
що утворюються при кожному введенні числа. Вихід з першого циклу здійснюємо, якщо ми ввели число 0.

Тести використовують дві тестові послідовності чисел:

10, 13, 73, 0 і чекають на суму 2847
1, 2, 3, 4, 0 і чекають на суму 20'''

'''
num = int(input("Enter integer (0 for output): "))
sum = 0
while
    for
        
    num = int(input("Enter integer (0 for output): "))
'''

num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    sum1=0
    for i in range(num+1):
        sum1 = sum1 + i
    sum = sum + sum1
        
    num = int(input("Enter integer (0 for output): "))