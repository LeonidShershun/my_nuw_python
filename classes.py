from collections import UserDict
from datetime import datetime
import pickle
import datetime
import difflib
import re
from prompt_toolkit.completion import Completer, Completion


class Field:
    def __init__(self, value=None):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class Name(Field):
    def __init__(self, value):
        self._value = value

    def validate(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("The name must be a non-empty string.")

        return self._value

    def __str__(self) -> str:
        return str(self._value)


class Phone(Field):
    def __init__(self, value):
        self._phone = None
        self.phone = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value:
            print(f"You have not entered a phone number.")
            self._phone = ""
        else:
            self._phone = self.correct(value)

    def correct(self, value):
        while True:
            correct_chars = ("(", ")", "-", " ")
            for i in correct_chars:
                value = str(value).replace(i, "")

            if len(value) == 13 and value.startswith("+38"):
                return value
            elif len(value) == 12 and value.startswith("38"):
                return f"+{value}"
            elif len(value) == 11 and value.startswith("80"):
                return f"+3{value}"
            elif len(value) == 10 and value.startswith("0"):
                return f"+38{value}"
            else:
                value = input(
                    f'Number "{value}" is not correct. Enter a valid phone number or press enter to skip: '
                )
                if not value:
                    print(f"You have not entered a phone number.")
                    return ""

    def __len__(self):
        return len(str(self._phone))

    def __str__(self) -> str:
        return str(self._phone)


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.set_date(value)

    def adjust_two_digit_year(self, value):
        separators = ["-", "/", ".", " "]
        current_full_year = datetime.datetime.now().year
        current_year = current_full_year % 100

        for sep in separators:
            parts = str(value).split(sep)
            if len(parts) == 3:
                if len(parts[2]) == 2:
                    if int(parts[2]) > current_year:
                        parts[2] = "19" + parts[2]
                    else:
                        parts[2] = "20" + parts[2]
                if len(parts[0]) == 2 and len(parts[2]) == 1:
                    if int(parts[0]) > current_year:
                        parts[0] = "19" + parts[0]
                    else:
                        parts[0] = "20" + parts[0]
                return sep.join(parts)
        return value

    def parse_date(self, value, formats):
        for date_format in formats:
            try:
                parsed_date = datetime.datetime.strptime(str(value), date_format)
                if parsed_date.date() <= datetime.datetime.now().date():
                    return parsed_date
                else:
                    print(f'Date is in the future: "{value}".')
            except ValueError:
                continue
        return None

    def set_date(self, original_value):
        formats = [
            "%d-%m-%Y",
            "%d-%m-%y",
            "%Y-%m-%d",
            "%y-%m-%d",
            "%d-%B-%Y",
            "%d-%B-%y",
            "%d-%b-%Y",
            "%d-%b-%y",
            "%d/%m/%Y",
            "%d/%m/%y",
            "%Y/%m/%d",
            "%y/%m/%d",
            "%d/%B/%Y",
            "%d/%B/%y",
            "%d/%b/%Y",
            "%d/%b/%y",
            "%d %m %Y",
            "%d %m %y",
            "%Y %m %d",
            "%y %m %d",
            "%d %B %Y",
            "%d %B %y",
            "%d %b %Y",
            "%d %b %y",
            "%d.%m.%Y",
            "%d.%m.%y",
            "%Y.%m.%d",
            "%y.%m.%d",
            "%d.%B.%Y",
            "%d.%B.%y",
            "%d.%b.%Y",
            "%d.%b.%y",
        ]

        value = self.adjust_two_digit_year(original_value)
        parsed_date = self.parse_date(value, formats)

        if parsed_date:
            self.__value = parsed_date
        else:
            print(f'Invalid date format for Birthday: "{original_value}".')
            return None

    def __str__(self) -> str:
        return self.__value.strftime("%d-%m-%Y") if self.__value else ""

    def __repr__(self) -> str:
        return self.__value.strftime("%d-%m-%Y") if self.__value else ""


class Address(Field):
    def __init__(self, value=None):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self._value)


class Email(Field):
    def __init__(self, value):
        self._value = None
        self.value = str(value).strip()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        while True:
            if not new_value:  # if the user left the field blank
                self._value = ""
                print(f"You have not entered an e-mail.")
                break
            if self.analyze_email(new_value):
                self._value = new_value
                break
            else:
                new_value = input(
                    "Invalid e-mail address. Enter a valid e-mail, or press enter to skip: "
                ).strip()

    @staticmethod
    def analyze_email(email):
        pattern = r"(^[a-zA-Z0-9_.+-]{2,}@([a-zA-Z0-9-]{2,}\.[a-zA-Z0-9]+$|[a-zA-Z0-9-]{2,}\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+$))"
        return re.match(pattern, email) is not None

    def __str__(self) -> str:
        return str(self._value)


class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"{self.title}: {self.content}"


class Tag:
    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return self.tag


class Record:
    def __init__(
        self,
        name: Name,
        phone: Phone = None,
        birthday: Birthday = None,
        address: Address = None,
        email: Email = None,
        phones=None,
        notes=None,
        tags=None,
    ):
        self.name = name
        self.phones = phones if phones is not None else []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
        self.address = address
        self.email = email
        self.notes = notes if notes is not None else []
        self.tags = tags if tags else []

    def add_phone(self, phone=None, birthday=None):
        if phone and self.phones not in [p for p in self.phones]:
            self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def del_phone(self, phone: Phone):
        for p in self.phones:
            if p.phone == phone.phone:
                self.phones.remove(p)
                return f'phone "{phone}" removed from contact "{self.name}".\n'
            return f'"{phone}" not present in phones of contact "{self.name}".\n'

    def del_contact(self, name):
        for name in self:
            self.remove(name)
            return f'Removed contact "{self.name}".\n'

    def edit_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if str(old_phone) == str(p):
                self.phones[idx] = new_phone
                return f'The old phone number "{old_phone}" has been updated to "{new_phone}" for contact "{self.name}".\n'
        return f'The phone number "{old_phone}" is not present in phones of contact "{self.name}".\n'

    def age_at_next_birthday(self):
        today = datetime.date.today()
        current_year_birthday = datetime.date(
            today.year, self.birthday.value.month, self.birthday.value.day
        )
        if today <= current_year_birthday:
            age = today.year - self.birthday.value.year
        else:
            age = today.year - self.birthday.value.year + 1
        return age

    def days_to_birthday(self):
        today = datetime.date.today()
        next_birthday = datetime.date(
            today.year, self.birthday.value.month, self.birthday.value.day
        )
        if today > next_birthday:
            next_birthday = datetime.date(
                today.year + 1, self.birthday.value.month, self.birthday.value.day
            )

        days_to_birthday = (next_birthday - today).days
        age = self.age_at_next_birthday()
        is_anniversary = age % 10 == 0
        anniversary_text = " (Jubilee!)" if is_anniversary else ""

        return days_to_birthday, age, anniversary_text

    def add_note(self, title, content):
        note = f"{title}: {content}"
        if hasattr(self, "notes"):
            self.notes.append(note)
        else:
            self.notes = [note]

    def edit_note(self, original_text, new_text):
        for index, note in enumerate(self.notes):
            if note == original_text:
                self.notes[index] = new_text
                return

    def show_notes(self):
        if not self.notes:
            return f'No notes found for "{self.name}".'
        notes_string = ""
        for idx, note in enumerate(self.notes, 1):
            notes_string += f'Note "{idx}": "{note.text}"\n'
        return notes_string.strip()

    def delete_note(self, note_index):
        if 0 <= note_index < len(self.notes):
            self.notes.pop(note_index)

    def add_tag(self, keyword):
        tag = Tag(keyword)
        if tag not in self.tags:
            self.tags.append(tag)

    def delete_tag(self, keyword):
        for tag in self.tags:
            if tag.keyword == keyword:
                self.tags.remove(tag)

    def change_email(self, new_email):
        if isinstance(new_email, Email):
            self.email = new_email
            return f"Email for contact {self.name} changed to {new_email}."
        else:
            raise ValueError("Invalid email type.")

    def __str__(self):
        phones_str = ", ".join(str(p) for p in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"


class CommandCompleter(Completer):
    def __init__(self, commands_dict):
        self.commands_dict = commands_dict
        self.commands = list(commands_dict)

    def get_completions(self, document, complete_event):
        word_before_cursor = document.text_before_cursor.lower().strip()
        matches = self._get_matches(word_before_cursor)
        for cmd in matches:
            yield Completion(
                cmd,
                start_position=-len(word_before_cursor),
                display_meta=self.commands_dict[cmd],
            )

    def _get_matches(self, text):
        if not text:
            return self.commands

        return [command for command in self.commands if command.startswith(text)]


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f'Contact "{record}" add success'

    def delete_record(self, name):
        del self.data[name]

    def delete_by_name(self, name: str):
        name_to_delete = next(
            (key for key in self.data.keys() if str(key).lower() == name.lower()), None
        )
        if name_to_delete:
            del self.data[name_to_delete]
            return f'Contact "{name_to_delete}" was successfully deleted.'
        else:
            return f'Contact "{name}" not found.'

    def edit_record(self, name, new_record):
        self.data[name] = new_record

    def search_records(self, **kwargs):
        results = []
        for record in self.data.values():
            match = True
            for key, value in kwargs.items():
                if key == "name":
                    if str(record.name).lower() != value.lower():
                        match = False
                        break
                elif key == "phone":
                    phone_match = False
                    for phone in record.phones:
                        if str(phone).lower() == value.lower():
                            phone_match = True
                            break
                    if not phone_match:
                        match = False
                        break
            if match:
                results.append(record)
        return results

    def search_by_name(self, name_query):
        results = []
        for record in self.data.values():
            if name_query.lower() in str(record.name).lower():
                results.append(record)
        return results

    def search_by_phone(self, phone_query):
        results = []
        for record in self.data.values():
            for phone in record.phones:
                if phone_query in str(phone):
                    results.append(record)
                    break
        return results

    def save_to_file(self, file_path):
        with open(file_path, "wb") as f:
            pickle.dump(self.data, f)

    def load_from_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = {}

    def contacts_with_upcoming_birthdays(self, days_left):
        upcoming_birthdays = []
        today = datetime.date.today()

        for record in self.data.values():
            if record.birthday:
                current_year_birthday = datetime.date(
                    today.year, record.birthday.value.month, record.birthday.value.day
                )
                if today > current_year_birthday:
                    current_year_birthday = datetime.date(
                        today.year + 1,
                        record.birthday.value.month,
                        record.birthday.value.day,
                    )

                days_until_birthday = (current_year_birthday - today).days
                if int(days_until_birthday) <= int(days_left):
                    upcoming_birthdays.append((record.name, days_until_birthday))

        return upcoming_birthdays

    def search_by_note(self, query):
        results = []
        for record in self.iterator():
            if record.note and query in record.note.text:
                results.append(record)
        return results

    def search_by_tag(self, keyword):
        results = []
        for record in self.iterator():
            for tag in record.tags:
                if tag.keyword == keyword:
                    results.append(record)
        return results

    def iterator(self, batch_size, page_number):
        data_values = list(self.data.values())
        start_idx = page_number * batch_size
        end_idx = min((page_number + 1) * batch_size, len(data_values))
        return data_values[start_idx:end_idx]

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())


from abc import ABC, abstractmethod


class BaseView(ABC):
    @abstractmethod
    def output(self, message: str):
        pass

    @abstractmethod
    def input(self, prompt: str) -> str:
        pass

    @abstractmethod
    def show_contact(self, contact: dict):
        pass

    @abstractmethod
    def show_notes(self, notes: list):
        pass

    @abstractmethod
    def show_commands(self, commands: dict):
        pass


class ConsoleView(BaseView):
    def output(self, message: str):
        print(message)

    def input(self, prompt: str) -> str:
        return input(prompt)

    def show_contact(self, contact: dict):
        for key, value in contact.items():
            self.output(f"{key}: {value}")

    def show_notes(self, notes: list):
        for note in notes:
            self.output(note)

    def show_commands(self, commands: dict):
        for command, desc in commands.items():
            self.output(f"{command} -> {desc}")
