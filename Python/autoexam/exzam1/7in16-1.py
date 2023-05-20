'''На цю мить у нас є три змінні: first_name, last_name та full_name

Додамо змінну message, яка фактично буде прототипом шаблонного листа користувачеві, який купив квиток.
Цю змінну ми сформуємо за допомогою f-рядка. У змінну message ми, за допомогою f-рядка, помістимо рядок наступного змісту:

"Dear <підставляємо first_name>, we inform you that you have purchased a ticket to travel to the island of Mauritius.
Departure June 31 of this year. Have a passport at <підставляємо full_name>. We are looking forward to seeing you!"'''

'''
first_name = "Stepan"
last_name = "Bandera"
full_name = first_name + " " + last_name
message =
'''

first_name = "Stepan"
last_name = "Bandera"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"