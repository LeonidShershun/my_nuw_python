import pickle
import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from functools import wraps
import sort_clean_folder


from classes import (
    AddressBook,
    Name,
    Phone,
    Record,
    Birthday,
    Address,
    Email,
    CommandCompleter,
    ConsoleView,
)

address_book = AddressBook()


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a command."
        except TypeError:
            return func()

    return wrapper


# view = ConsoleView()


@input_error
def add_contact():
    """Adds a new contact."""
    name = input("Enter the name: ").strip()
    if not name:
        print("You cannot create a contact without a name.")
        main()
    else:
        name = Name(name)
    rec: Record = address_book.get(str(name))
    if rec:
        return "Contact already exists. Use 'edit phone', 'edit birthday', etc., to modify the contact."
    phone = input("Enter the phone, or press enter to skip: ").strip()
    if phone != "":
        phone = Phone(phone)
    else:
        print(f"You have not entered a number phone.")

    def birthday_input():
        birthday = input("Enter the date of birthday, or press enter to skip: ").strip()
        if birthday != "":
            birthday = Birthday(birthday)
            if len(str(birthday).split("-")) != 3:
                birthday_input()
            else:
                return birthday
        else:
            print(f"You have not entered a date of birthday.")
            return

    birthday = birthday_input()
    address = input("Enter the address, or press enter to skip: ").strip()
    if address != "":
        address = Address(address)
    else:
        print(f"You have not entered the adress.")
    email = input("Enter the e-mail, or press enter to skip: ").strip()
    if email != "":
        email = Email(email)
    else:
        print(f"You have not entered an e-mail.")
    rec = Record(name, phone, birthday, address, email)
    address_book.add_record(rec)
    return f'Contact "{name}" successfully added.\n'


@input_error
def hello():
    """Displays a welcome message."""
    return "Hello! How can I help you?\n"


@input_error
def del_phone():
    """Delete number phone from contact."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot delete phone a contact without a name.\n")
        main()
    phone_del = Phone(input(f'Enter the number to remove from "{name}" contact: '))
    rec: Record = address_book.get(str(name))
    if rec:
        rec.del_phone(phone_del)
        return f'The phone number "{phone_del}" has been removed from the contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


@input_error
def del_contact():
    """Delete full information from contact."""
    name = input("Enter the name of the contact you want to delete: ").strip()
    if not name:
        return "You cannot delete a contact without a name.\n"
    name_obj = Name(name)
    if str(name_obj) in address_book.data:
        del address_book.data[str(name_obj)]
        return f'Contact "{name}" was successfully deleted.\n'
    else:
        return f'Contact "{name}" not found in the address book.\n'


@input_error
def add_phone():
    """Adds phone to existing contact."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot added phone a contact without a name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec:
        new_phone = Phone(input(f'Enter fone for "{name}": '))
        rec.add_phone(new_phone)
        return f'Phone number "{new_phone}" added to contact "{name}".\n'
    return f'No contact "{name}" in the address book.\n'


@input_error
def edit_phone():
    """Changes the phone number of an existing contact."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot change phone a contact without a name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec:
        phone_input = Phone(input(f'Enter number phone for "{name}": '))
        new_phone = phone_input
        rec.add_phone(new_phone)
        return f'Phone number "{new_phone}" added to contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


@input_error
def change_phone():
    """Replaces the old number with a new one."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot change phone a contact without a name.\n")
        main()
    old_phone = Phone(input(f'Enter the old phone number for "{name}": '))
    new_phone = Phone(input(f'Enter the new phone number for "{name}": '))
    rec: Record = address_book.get(str(name))
    if rec:
        print(rec.edit_phone(old_phone, new_phone))
    return ""


@input_error
def add_birthday():
    """Adds birthday to contact."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot added birthday a contact without a name.\n")
        main()
    birthday = Birthday(input(f'Enter birthday for "{name}": ').strip())
    rec: Record = address_book.get(str(name))
    if rec:
        rec.birthday = birthday
        return f'Birthday "{birthday}" updated for contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


@input_error
def days_to_birthday():
    """Shows how many days are left until the birthday."""
    day_period = int(input("Enter the number of days to look ahead: "))
    results = []

    for name, record in address_book.data.items():
        days_left, age, anniversary_text = record.days_to_birthday()
        if days_left <= day_period:
            results.append(
                f'The birthday of the "{record.name}" contact is in "{days_left}" days. Turning {age} years old{anniversary_text}.'
            )

    if results:
        return "\n".join(results)
    else:
        return "No contacts have birthdays in the specified period."


@input_error
def edit_birthday():
    """Changes the existing birthday value of a contact."""
    name = input("Enter the name: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot added birthday a contact without a name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec:
        new_birthday = Birthday(input(f'Enter a new birthday for "{name}": ').strip())
        rec.birthday = new_birthday
        return f'Birthday updated for contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


@input_error
def show_all():
    """Displays all contacts with full information."""
    page_number = 1
    batch_size = 6
    while True:
        records_batch = list(address_book.iterator(batch_size, page_number - 1))
        if not records_batch:
            print("No more contacts to display.")
            break
        for record in records_batch:
            birthday_info = (
                f"birthday: {str(record.birthday.value).split()[0]}, "
                if record.birthday
                else ""
            )
            phones_info = (
                f"phones: {' / '.join(str(phone) for phone in record.phones)}, "
                if record.phones
                else ""
            )
            address_info = f"address: {record.address}, " if record.address else ""
            email_info = f"email: {record.email.value}." if record.email else ""
            print(
                f'Contact: => name "{record.name}" {phones_info}{birthday_info}{address_info}{email_info}'
            )
        print("\nPage:", page_number)
        user_input = input(
            'Press Enter to see the next page or type "exit" to return to the main menu.\n'
        ).strip()
        if user_input.lower().strip() == "exit":
            break
        else:
            page_number += 1
    return "Continue...\n"


def search_by_name():
    """Searches for contacts by name."""
    name_query = input("Enter the name or part of the name to search: ").strip()
    results = address_book.search_by_name(name_query)
    if results:
        return "\n".join(str(record) for record in results)
    return "No contacts found for the given name.\n"


def search_by_phone():
    """Looks for contacts with a matching phone number."""
    phone_query = input("Enter the phone or part of the phone to search: ").strip()
    results = address_book.search_by_phone(phone_query)
    if results:
        return "\n".join(str(record) for record in results)
    return "No contacts found for the given phone."


def add_note():
    """Adds a note to a contact."""
    name = input("Enter the name of the contact to add a note: ").strip()
    if not name:
        return "You cannot add a note without specifying a contact name.\n"
    name = Name(name)
    rec: Record = address_book.get(str(name))
    if rec:
        title = input("Enter the Title of the note: ")
        content = input("Enter the content of the note: ")
        rec.add_note(title, content)
        return f'Note "{title}" added to contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


def edit_note():
    """Edits a note in a contact."""
    name = input("Enter the name of the contact to edit a note: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot edit a note without specifying a contact name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec and rec.notes:
        print("Here are the current notes for this contact:")
        for index, note in enumerate(rec.notes, start=1):
            print(f"{index}. {note}")
        note_index = int(
            input(f"Which note do you want to edit (1-{len(rec.notes)})? ")
        )
        original_note_text = rec.notes[note_index - 1]
        new_note_text = input(f'Enter the new note for "{name}": ')
        rec.edit_note(original_note_text, new_note_text)
        return f'Note updated for contact "{name}".\n'
    return f'No contact "{name}" with a note in address book.\n'


def add_tag():
    """Adds a tag to a contact."""
    name = input("Enter the name of the contact to add a tag: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot add a tag without specifying a contact name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec:
        tag_text = input(f'Enter the tag for "{name}": ')
        rec.add_tag(tag_text)
        return f'Tag added to contact "{name}".\n'
    return f'No contact "{name}" in address book.\n'


def search_by_note():
    """Search contacts by note content."""
    query = input("Enter text to search for in notes: ").strip()
    results = address_book.search_by_note(query)
    if results:
        return "\n".join(str(record) for record in results)
    return "No contacts found with the given note text.\n"


def search_by_tag():
    """Search contacts by tags."""
    keyword = input("Enter tag to search for: ").strip()
    results = address_book.search_by_tag(keyword)
    if results:
        return "\n".join(str(record) for record in results)
    return "No contacts found with the given tag.\n"


@input_error
def show_notes_for_all():
    """Shows all notes for all contacts."""
    results = []
    for record in address_book.iterator(10000, 0):  # Assuming a max of 10,000 records.
        if hasattr(record, "notes") and record.notes:
            for note in record.notes:
                results.append(f'Contact: "{record.name}", Note: "{note}"')
    if results:
        return "\n".join(results)
    return "No notes found."


@input_error
def show_notes_for_contact():
    """Shows notes for a specific contact."""
    name_query = input("Enter the name of the contact to show notes: ").strip()
    rec: Record = address_book.get(str(name_query))
    if rec and rec.note:
        return f"Notes for {rec.name}: {rec.note}"
    return f"No notes found for contact {name_query}."


def delete_note():
    """Delete a note from a contact."""
    name = input("Enter the name of the contact to delete a note: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot delete a note without specifying a contact name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec and rec.notes:
        print("Here are the current notes for this contact:")
        for index, note in enumerate(rec.notes, start=1):
            print(f"{index}. {note}")
        note_index = int(
            input(f"Which note do you want to delete (1-{len(rec.notes)})? ")
        )
        rec.delete_note(note_index - 1)
        return f'Note deleted for contact "{name}".\n'
    return f'No contact "{name}" with a note in address book.\n'


def delete_tag():
    """Delete a tag from a contact."""
    name = input("Enter the name of the contact to delete a tag: ").strip()
    if name != "":
        name = Name(name)
    else:
        print("You cannot delete a tag without specifying a contact name.\n")
        main()
    rec: Record = address_book.get(str(name))
    if rec and rec.tags:
        tag_text = input(f'Enter the tag you want to delete from "{name}": ')
        rec.delete_tag(tag_text)
        return f'Tag "{tag_text}" deleted from contact "{name}".\n'
    return f'No contact "{name}" with the specified tag in address book.\n'


def helper():
    """Displays the list of available commands."""
    help_text = "\nAvailable commands:\n"
    for command, description in COMMAND_DES.items():
        help_text += f'Command: "{command}"  -->  {description}\n'
    return help_text


@input_error
def show_contact():
    """Displays detailed information about a specific contact."""
    name = input("Enter the name of the contact: ").strip()
    if name != "":
        name = Name(name)
    else:
        print(
            "You cannot detailed information about a specific contact without specifying a contact name.\n"
        )
        main()
    rec: Record = address_book.get(str(name))
    if not rec:
        return f'Contact "{name}" not found.'
    birthday_info = (
        f"birthday: {str(rec.birthday.value).split()[0]}, " if rec.birthday else ""
    )
    phones_info = (
        f"phones: {' / '.join(str(phone) for phone in rec.phones)}, "
        if rec.phones
        else ""
    )
    address_info = f"address: {rec.address}, " if rec.address else ""
    email_info = f"email: {rec.email.value}." if rec.email else ""
    notes_info = (
        '"\n"'.join(str(note) for note in rec.notes)
        if hasattr(rec, "notes") and rec.notes
        else ""
    )
    tags_info = ", ".join(rec.tags) if hasattr(rec, "tags") and rec.tags else ""
    return (
        f'Contact: => name "{rec.name}" {phones_info}{birthday_info}{address_info}{email_info}\n'
        f'Notes: "{notes_info}"\n'
        f'Tags: "{tags_info}"'
    )


def find_matching_commands(text, commands):
    available_commands = list(commands.keys())
    matching_commands = difflib.get_close_matches(
        text.lower(), available_commands, n=99, cutoff=0.3
    )
    return matching_commands


COMMAND_DES = {
    "hello": "Displays a welcome message.",
    "add": "Add a new contact.",
    "add phone": "Add a phone number to an existing contact.",
    "add birthday": "Add birthday to contact.",
    "edit birthday": "Replace the current value of the contact's birthday.",
    "days to birthday": "Shows how many days are left until the birthday for the specified number of days from the current date.",
    "edit phone": "Changes the phone number of an existing contact.",
    "del phone": "Delete number from contact.",
    "del contact": "Delete contact.",
    "change phone": "Replaces the old number with a new one.",
    "show all": "Displays all contacts and the full available contact information.",
    "search by name": "Search contacts by name.",
    "search by phone": "Searches for contacts by matching phone number or part of it.",
    "help": "Displays a list of available commands.",
    "exit": "Exit the program.",
    "good bye": "Exit the program.",
    "close": "Exit the program.",
    "add note": "Adds a note to the contact.",
    "edit note": "Edits a note in a contact.",
    "delete note": "Delete a note from a contact.",
    "add tag": "Adds a tag to a contact.",
    "delete tag": "Delete a tag from a contact.",
    "search by note": "Search contacts by note content.",
    "search by tag": "Search contacts by tags.",
    "show all notes": "Shows all notes for all contacts.",
    "show contact": "Displays detailed information about a specific contact.",
    "show notes for contact": "Shows notes for a specific contact.",
    "sort": "Sort files by type and folders in the specified folder.",
    "change email": "Change e-mail",
}


def completer(text, state):
    options = [i for i in COMMAND_DES.keys() if i.startswith(text)]
    if state < len(options):
        return options[state]
    return None


# readline.parse_and_bind("tab: complete")
# readline.set_completer(completer)


def sort():
    folder_path = input(
        "Enter the exact address of the folder whose contents you want to sort: "
    )
    a = sort_clean_folder.main(folder_path)
    print(a)
    # return "Alright, sorting done!"


def exit_program():
    """Exit the program."""
    print("\nOkay, I'm going to rest... Get in touch if you need to... See you soon!\n")
    exit()


def change_email_command():
    """Change e-mail"""
    name = input("Enter the name of the contact you want to change the e-mail for: ")
    new_email = Email(input("Enter the new email: "))
    contacts = address_book.search_by_name(name)
    if contacts:
        contact = contacts[0]
        email = Email(new_email)
        contact.change_email(email)
        return f'Email for "{name}" changed to "{new_email}".'
    else:
        return f'Contact with the name "{name}" not found.'


def main():
    file_path = "address_book.pkl"
    view = ConsoleView()
    try:
        address_book.load_from_file(file_path)
    except pickle.UnpicklingError:
        view.output(
            "Failed to load the address book. Starting with an empty address book."
        )
    commands = {
        "hello": hello,
        "add": add_contact,
        "add phone": add_phone,
        "add birthday": add_birthday,
        "change email": change_email_command,
        "edit birthday": edit_birthday,
        "days to birthday": days_to_birthday,
        "edit phone": edit_phone,
        "del phone": del_phone,
        "del contact": del_contact,
        "change phone": change_phone,
        "show all": show_all,
        "search by name": search_by_name,
        "search by phone": search_by_phone,
        "help": helper,
        "exit": exit_program,
        "good bye": exit_program,
        "close": exit_program,
        "add note": add_note,
        "edit note": edit_note,
        "delete note": delete_note,
        "add tag": add_tag,
        "delete tag": delete_tag,
        "search by note": search_by_note,
        "search by tag": search_by_tag,
        "show all notes": show_notes_for_all,
        "show contact": show_contact,
        "show notes for contact": show_notes_for_contact,
        "sort": sort,
    }

    def get_completions(text):
        words = text.split()
        if not words:
            return [f"{command} - {desc}" for command, desc in COMMAND_DES.items()]
        last_word = words[-1]
        if len(words) == 1:
            return [
                f"{command} - {desc}"
                for command, desc in COMMAND_DES.items()
                if command.startswith(last_word)
            ]
        else:
            potential_matches = [
                command for command in COMMAND_DES.keys() if command.startswith(text)
            ]
            return [f"{match} - {COMMAND_DES[match]}" for match in potential_matches]

    completer = CommandCompleter(COMMAND_DES.keys())

    while True:
        command = view.input("\nEnter a command: ").lower()
        if command in commands:
            func = commands[command]
            print(func())
        else:
            matching_commands = find_matching_commands(command, commands)
            if matching_commands:
                print(f"Did you mean one of these commands?")
                for match in matching_commands:
                    print(
                        f"-> {match}: {commands[match].__doc__}"  # Використовуйте docstring для опису команди
                    )
            else:
                print("Invalid command. Please try again.")
        address_book.save_to_file(file_path)


if __name__ == "__main__":
    print(
        """
Welcome!

I AM YOUR PERSONAL ASSISTANT
GLAD TO BE HELPFUL TO YOU!"""
    )
    main()
