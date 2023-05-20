'''Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами, 
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишіть функцію format_ingredients, яка прийматиме на вхід список з 
інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок 
зібраний з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.'''

'''
def format_ingredients(items):
'''

def format_ingredients(items):
    a=len(items)
    if a <=1:
        return ', '.join(items)
    else:
        items[-2] = items[-2] +  ' and '
        return ', '.join(items[:-1]) + items[-1]