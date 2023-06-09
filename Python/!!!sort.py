'''Скрипт повинен проходити по вказаній під час виклику папці та сортирувати всі файли за групами:

зображення ('JPEG', 'PNG', 'JPG', 'SVG');
відео файли ('AVI', 'MP4', 'MOV', 'MKV');
документи ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
музика ('MP3', 'OGG', 'WAV', 'AMR');
архіви ('ZIP', 'GZ', 'TAR');
невідомі розширення.

Вимоги до функції normalize:

приймає на вхід рядок та повертає рядок;
здійснює транслітерацію кириличних символів на латиницю;
замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
транслітерація може не відповідати стандарту, але бути читабельною;
великі літери залишаються великими, а маленькі — маленькими після транслітерації.

Умови для обробки:
зображення переносимо до папки images
документи переносимо до папки documents
аудіо файли переносимо до audio
відео файли до video
архіви розпаковуються та їх вміст переноситься до папки archives

Критерії приймання завдання
всі файли та папки перейменовуються за допомогою функції normalize.
розширення файлів не змінюється після перейменування.
порожні папки видаляються
скрипт ігнорує папки archives, video, audio, documents, images;
розпакований вміст архіву переноситься до папки archives у підпапку, названу так само, як і архів,
але без розширення в кінці;
файли, розширення яких невідомі, залишаються без зміни.'''

import re

string = 'Cаме баран починкабанається кабан з каБан , яке Баран є числом кАбан.'
repl = '***'
a = "кабан"
print(re.sub(a, repl, string, flags=re.IGNORECASE))