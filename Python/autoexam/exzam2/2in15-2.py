'''У нас є три логічні змінні.

Перша визначає статус користувача is_active, яка дорівнює True або False.
Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
Третя is_permission — чи дозволено доступ, теж булевого типу.
Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

Надайте змінній access, значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.

Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.

Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True'''

'''
is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

access =
'''

is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
access = False
is_admin = bool(is_admin)
is_active = bool(is_active)
is_permission = bool(is_permission)
if is_admin:
    access = True