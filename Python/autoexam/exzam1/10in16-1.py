'''Необхідно обчислити корені квадратного рівняння.

a · x2 + b · x + c = 0

Задайте змінні коефіцієнти a, b, c зі значеннями -2, 7, -6 відповідно

Дискримінант рівняння помістіть у змінну D

D = b2 - 4 · a · c

Корені рівняння помістіть у змінні x1 та x2, відповідно.

x1 = (-b + D0.5) / (2 · a)

x2 = (-b - D0.5) / (2 · a)'''

'''
import math

a = -2
b = 7
c = -6
D =
x1 =
x2 =
'''

import math
a = -2
b = 7
c = -6
D = b**2 - 4 * a * c
x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)