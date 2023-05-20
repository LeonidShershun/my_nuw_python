'''Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок
Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код.

Компанія працює з наступними країнами

Країна	   Код ISO	Префікс
Japan	     JP	     +81
Singapore	 SG	     +65
Taiwan	     TW	     +886
Ukraine	     UA	     +380

Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список
телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції
sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку
словника з ключем 'UA'.'''

'''
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
'''

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    phone_numbers = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
        }
    
    port_phone = [sanitize_phone_number(phone) for phone in list_phones]
    for phone in port_phone:
        if phone[:1] == '0' or phone[:3] == '380':
            phone_numbers["UA"].append(phone)
        elif phone[:3] == '886':
            phone_numbers["TW"].append(phone)
        elif phone[:2] == '81':
            phone_numbers["JP"].append(phone)
        elif phone[:2] == '65':
            phone_numbers["SG"].append(phone)

    return phone_numbers


list_phones = (['0658759411', '818765347', '818765344', '8867658976', '657658976'])
print(get_phone_numbers_for_countries(list_phones))