'''ЗАВДАННЯ: СТРУКТУРУЄМО ЗАПИС У ФАЙЛ
Задано відомість абітурієнтів, які склали вступні іспити до університету. Структура даних щодо абітурієнтів
подана у вигляді наступного списку:

[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, на яку він
поступив — ключ specialty, та отримані ним бали з окремих дисциплін — ключі math (математика), lang ( українська
мова) та eng (англійська мова)

Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра source зберігати
у файл із параметра output

Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні бути записані
через кому без прогалин прізвище абітурієнта, код спеціальності, на яку він поступив, та отримані ним бали
за окремими дисциплінами.

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Karpenko Dmitro,201,155,175,185

Вимоги:

відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
запис нового вмісту файлу output має бути або за допомогою методу writelines, або використовувати метод write
'''

'''
def save_applicant_data(source, output):
'''



def save_applicant_data(source, output):
    # with open(source, 'r') as fh:
    #     data = fh.read()
    #     print(data)
    with open(output, 'w') as fh:
        for applicant in source:
            line = f"{applicant['name']},{applicant['specialty']},{applicant['math']},{applicant['lang']},{applicant['eng']}\n"
            print(line)
            fh.write(line)
    
            







#source = 'test.txt' 
output = 'test_for_file8.txt'
print()

#print(save_applicant_data(source, output))
print()
source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
# '''Kovalchuk Oleksiy,301,175,180,155
# Ivanchuk Boryslav,101,135,150,165
# Karpenko Dmitro,201,155,175,185'''
save_applicant_data(source, output)
print()