from typing import List, Union

from .address_book import AddressBook
from .auxiliary_functions import find_users, forming_user_information, find_notes
from .class_note import Note
from .classes_address_book import Record
from .constant_config import (
    AMBUSH,
    LIMIT_RECORDS_TO_DISPLAY,
    OTHER_MESSAGE, 
    WARNING_MESSAGE, 
)
from .main_validator import input_error
from .note_book import NoteBook
from .serialization import SaveTheBook

from junk_sorter import junk_sorter

@input_error
def handler_add_address(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add address...": The bot saves new information about user 
    in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and address (simple string), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and address).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    # verdict = contact_dictionary[name].add_address(user_command[2])
    verdict = contact_dictionary[name].add_address(' '.join(user_command[2:]))

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_add_birthday(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add birthday...": The bot saves new information about user 
    in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and birthday (in format YYYY-MM-DD), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and birthday).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    verdict = contact_dictionary[name].add_birthday(user_command[2])

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_add_details(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add details...": The bot saves new information about user 
    in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name, type details info and details info, 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user, type details info 
                and details info).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    verdict = contact_dictionary[name].details.add_details(user_command[2], ' '.join(user_command[3:]))

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_add_email(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add ...": The bot saves a new emails to contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name
    and email(s), necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and email(s)).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    emails = user_command[2:]
    verdict = False
    write_count = 0

    for new_email in emails:
        verdict = contact_dictionary[name].add_email(new_email) or verdict
        write_count += 1 if verdict else 0

    if not write_count:
        return OTHER_MESSAGE.get('no new entries', [AMBUSH])[0]

    if SaveTheBook().save_book(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_add_nickname(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add nickname...": The bot saves new information about user 
    in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and nickname, 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and nickname).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    verdict = contact_dictionary[name].add_nickname(user_command[2])

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_add_phone(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add ...": The bot saves a new phones to contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name
    and phone number(s), necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and phone(s)).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    phones = user_command[2:]
    verdict = False
    write_count = 0

    for new_phone in phones:
        verdict = contact_dictionary[name].add_phone(new_phone) or verdict
        write_count += 1 if verdict else 0

    if not write_count:
        return OTHER_MESSAGE.get('no new entries', [AMBUSH])[0]

    if SaveTheBook().save_book(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_add(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"add ...": The bot saves a new contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters 
    the name and phone number(s), necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user [and phone(s)]).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    new_record = Record(name)
    contact_dictionary.add_record(new_record)

    if len(user_command) > 2:

        phones = user_command[2:]
        verdict = False

        for new_phone in phones:
            verdict = contact_dictionary[name].add_phone(new_phone) or verdict

        if not verdict:
            return WARNING_MESSAGE.get('empty record to add', AMBUSH)

    if SaveTheBook().save_book(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('successful addition', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_change_address(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change address ...": The bot stores the
    "new address" (if the previous one was wrong)
    of the existing contact in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and address (in format YYYY-MM-DD), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user, and address).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    user_address = ' '.join(user_command[2:])
    verdict = contact_dictionary[name].change_address(user_address)

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_change_birthday(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change birthday ...": The bot stores the
    "new birthday" (if the previous one was wrong)
    of the existing contact in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and birthday (in format YYYY-MM-DD), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user, and birthday).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    user_birthday = user_command[2]
    verdict = contact_dictionary[name].change_birthday(user_birthday)

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_change_details(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change details ...": The bot stores the new details of the existing 
    contact in contact dictionary and save it in file(path_file).
    Instead of ... the user enters the name, type details note and new details information, 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user, type details info 
                and details info).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    verdict = contact_dictionary[name].details.change_details(user_command[2], ' '.join(user_command[3:]))

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_change_email(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change ...": The bot stores the new email of the existing 
    contact in contact dictionary and save it in file(path_file).
    Instead of ... the user enters the name and email(s) (current and new), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and emails).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    current_email = user_command[2]
    new_email = user_command[3]
    verdict = contact_dictionary[name].change_email(current_email, new_email)

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_change_nickname(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change nickname ...": The bot stores the
    "new nickname" (if the previous one was wrong)
    of the existing contact in contact dictionary and save it in file(path_file). 
    Instead of ... the user enters the name and nickname, 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user, and nickname).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    user_nickname = user_command[2]
    verdict = contact_dictionary[name].change_nickname(user_nickname)

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


@input_error
def handler_change(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"change ...": The bot stores the new phone number of the existing 
    contact in contact dictionary and save it in file(path_file).
    Instead of ... the user enters the name and phone numbers (current and new), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user and phones).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    current_phone = user_command[2]
    new_phone = user_command[3]
    verdict = contact_dictionary[name].change_phone(current_phone, new_phone)

    if verdict[0]:

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


def handler_command_guesser(user_command: List[str], _=None, __=None) -> Union[str, None]:
    """In the case of an unrecognized command, the bot offers the closest similar known command."""
    candidates = user_command[1:]
    commands = []
    for word in candidates:
        for part in ALL_COMMAND:
            if part.startswith(word):
                commands.append(part.replace('_', ' '))
    if not commands:
        for word in candidates:
            for part in ALL_COMMAND:
                if word in part:
                    commands.append(part.replace('_', ' '))
    if not commands:
        for word in candidates:
            for part in ALL_COMMAND:
                if word[:3] in part:
                    commands.append(part.replace('_', ' '))
    if commands:
        return f'''{OTHER_MESSAGE.get('Unknown', [AMBUSH]*3)[2]}{commands}\n'''

    return OTHER_MESSAGE.get('Unknown', [AMBUSH])[0] + OTHER_MESSAGE.get('Unknown', [AMBUSH]*2)[1]


@input_error
def handler_email(user_command: List[str], contact_dictionary: AddressBook, _=None) -> str:
    """"email ...": The bot outputs the email for the specified
    contact. Instead of ... the user enters the name of the contact
    whose number should be displayed.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _: not matter (path_file (str): Is there path and filename of address book).

        Returns:
            string(str): Answer for the user (email(s) of user).
    """
    emails = ''
    name = user_command[1]

    for email in (contact_dictionary[name]).emails:
        emails += f'{email.value}; '

    return emails


def handler_exit(*_) -> str:
    """Reply to the exit command."""
    return OTHER_MESSAGE.get('Bye', [AMBUSH])[0]


@input_error
def handler_find(user_command: List[str], contact_dictionary: AddressBook, _=None) -> list:
    """"Find ...": The bot outputs a list of users whose name or phone number 
    matches the entered one or more(with an OR setting) string without space(' ').

        Parameters:
            user_command (List[str]): List of user command (string(s) for searching).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _: path_file (str) - Is there path and filename of address book.

        Returns:
            found_list (list): Answer for the user - list of string of found users.
    """ 
    found_list = [OTHER_MESSAGE.get('found', [AMBUSH])[0]]
 
    for records in contact_dictionary.iterator(LIMIT_RECORDS_TO_DISPLAY): 
        volume = ''

        for record in records:

            if find_users(user_command[1:], record):

                volume += forming_user_information(record)

        found_list.append(volume)

    return found_list

@input_error
def handler_happy_birthday(user_command: List[str], contact_dictionary: AddressBook, _=None) -> list:
    """"happy birthday ...": The bot outputs a list of users whose the birthday will be celebrated 
        between the current date and the specified day (consecutive days from the current date).
        End day must be between 1 and 90.
        Example:
            happy birthday 10

        Parameters:
            user_command (List[str]): List of user command (End day in [1]).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _: path_file (str) - Is there path and filename of address book.

        Returns:
            found_list (list): Answer for the user - list of string of found users with happy birthday.
    """ 
    return contact_dictionary.show_happy_birthday(user_command[1])


def handler_hello(*_) -> str:
    """Reply to the greeting."""
    return OTHER_MESSAGE.get('Hello', [AMBUSH])[0]


def handler_help(*_) -> str:
    """
    Return all known commands.
    """
    all_commands_list = [OTHER_MESSAGE.get('all commands list', [AMBUSH])[0]]
    all_commands_list += [f'''{key.replace('_',' ')}\n''' for key in ALL_COMMAND]
    return ''.join(all_commands_list)


@input_error
def handler_phone(user_command: List[str], contact_dictionary: AddressBook, _=None) -> str:
    """"phone ...": The bot outputs the phone number for the specified
    contact. Instead of ... the user enters the name of the contact
    whose number should be displayed.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _: not matter (path_file (str): Is there path and filename of address book).

        Returns:
            string(str): Answer for the user (phone number(s) of user).
    """
    phones = ''
    name = user_command[1]

    for phone in (contact_dictionary[name]).phones:
        phones += f'{phone.value}; '

    return phones


@input_error
def handler_remove_address(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove address ...": The bot remove a address record from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook .
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].address:

            contact_dictionary[name].remove_address()

            if SaveTheBook().save_book(contact_dictionary, path_file):
                return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
            else:
                return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

        else:
            address2 = OTHER_MESSAGE.get('Raddress', [AMBUSH]*3)[2]
            address3 = OTHER_MESSAGE.get('Raddress', [AMBUSH]*4)[3]
            return f'{address2}\"{name}\"{address3}'

    else:  # duplicate 'of except TheContactIsNotExist'
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove_birthday(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove birthday ...": The bot remove a birthday record from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook .
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].birthday:

            contact_dictionary[name].remove_birthday()

            if SaveTheBook().save_book(contact_dictionary, path_file):
                return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
            else:
                return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

        else:
            birthday2 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*3)[2]
            birthday3 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*4)[3]
            return f'{birthday2}\"{name}\"{birthday3}'

    else:  # duplicate 'of except TheContactIsNotExist'
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove_details(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove details ...": The bot remove a type details note from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name and type details note.

        Parameters:
            user_command (List[str]): List of user command (name of user, type details).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].details.get(user_command[2], None):

            verdict = contact_dictionary[name].details.remove_details()
            if not verdict[0]:
                return verdict[1]

            if SaveTheBook().save_book(contact_dictionary, path_file):
                return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
            else:
                return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

        else:
            details2 = OTHER_MESSAGE.get('RDetails', [AMBUSH]*3)[2]
            details3 = OTHER_MESSAGE.get('RDetails', [AMBUSH]*4)[3]
            return f'{details2}\"{name}\"{details3}'

    else:  # duplicate 'of except ....'
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove_email(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove email ...": The bot remove a email record from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name and email(s), 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].emails:

            email = user_command[2]
            verdict = contact_dictionary[name].remove_email(email)

            if verdict:

                if SaveTheBook().save_book(contact_dictionary, path_file):
                    return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
                else:
                    return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

            else:
                email2 = OTHER_MESSAGE.get('REmail', [AMBUSH]*3)[2]
                return f'\"{email}\"{email2}\"{name}\".'

        else:
            email1 = OTHER_MESSAGE.get('REmail', [AMBUSH]*2)[1]
            return f'{email1}\"{name}\".\n'

    else:
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove_nickname(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove nickname ...": The bot remove a nickname record from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook .
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].nickname:

            contact_dictionary[name].remove_nickname()

            if SaveTheBook().save_book(contact_dictionary, path_file):
                return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
            else:
                return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

        else:
            nickname2 = OTHER_MESSAGE.get('RNickname', [AMBUSH]*3)[2]
            return f'{nickname2}\"{name}\"'

    else:  # duplicate 'of except TheContactIsNotExist'
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove_phone(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove phone ...": The bot remove a phone record from contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name and phone 
    number(s), necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    if contact_dictionary.get(name, None):

        if contact_dictionary[name].phones:

            phone = user_command[2]
            verdict = contact_dictionary[name].remove_phone(phone)

            if verdict:

                if SaveTheBook().save_book(contact_dictionary, path_file):
                    return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
                else:
                    return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

            else:
                phone2 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*3)[2]
                return f'\"{phone}\"{phone2}\"{name}\".'

        else:
            phone1 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*2)[1]
            return f'{phone1}\"{name}\".\n'

    else:
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_remove(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"remove ...": The bot remove a record contact in contact dictionary 
    and save it in file(path_file). Instead of ... the user enters the name.

        Parameters:
            user_command (List[str]): List of user command (name of user).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]

    if contact_dictionary.get(name, None):

        contact_dictionary.remove_record(name)

        if SaveTheBook().save_book(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('deleting successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        return WARNING_MESSAGE.get('unknown name', AMBUSH)


@input_error
def handler_show_all(_, contact_dictionary: AddressBook, __) -> list:
    """"show all": The bot outputs all saved contacts.

        Parameters:
            _: not matter (user_command (List[str]): List of user command).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _a: not matter (path_file (str): Is there path and filename of address book).

        Returns:
            string(str): Answer for the user (list of string of all users).
    """
    all_list = [OTHER_MESSAGE.get('all list', [AMBUSH])[0]]

    for records in contact_dictionary.iterator(LIMIT_RECORDS_TO_DISPLAY):
        volume = ''

        for record in records:

            volume += forming_user_information(record)

        all_list.append(volume)

    return all_list


@input_error
def handler_show(user_command: List[str], contact_dictionary: AddressBook, _=None) -> str:
    """"show information about a specific user". With this command, the bot outputs
    birthday, number of days until next birthday and phone numbers to the console.

        Parameters:
            user_command (List[str]): List of user command (name of user [and phone(s)]).
            contact_dictionary (AddressBook): Instance of AddressBook.
            _: not matter (path_file (str): Is there path and filename of address book).

        Returns:
            string(str): Answer for the user (string of information about user).
    """
    name = user_command[1]

    return forming_user_information(contact_dictionary[name])


def secret_command(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> str:
    """"gen": The bot generate virtual persons with random data, only for testings. 

        Parameters:
            user_command (List[str]): List of user command (name of user and quantity).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            string(str): Answer for the user.
    """
    from random import randint, choice
    try:
        quantity = int(user_command[1]) if int(user_command[1]) > 0 else 24
    except (IndexError, ValueError) as error:
        # print(f'user command: {user_command[1]}, \n error: {repr(error)}')
        quantity = 100

    generators_names = [f'Name{item}' for item in range(quantity)]
    for name in generators_names:
        handler_add(['add', name], contact_dictionary, path_file)
        if randint(0,1):
            handler_add_nickname(['add_nickname', name, name+name[::-1]], contact_dictionary, path_file)
        if randint(0,1):    
            handler_add_birthday(['add_birthday', name, f'{randint(1970,2002)}-{randint(1,12)}-{randint(1,28)}'], contact_dictionary, path_file)
        if randint(0,1): 
            for _ in range(randint(1,5)):
                numder_ = str(randint(0,9)) * 7
                handler_add_phone(['add_phone', name, f'+380{choice([63,67,50,73,91,93,97])}{numder_}'], contact_dictionary, path_file)
        if randint(0,1): 
            for _ in range(randint(1,3)):
                domen = 'emaN'
                handler_add_email(['add_email', name, f'{name}@{domen*randint(1,3)}.com.ua'], contact_dictionary, path_file)
        if randint(0,1):
            handler_add_address(['add_address', name, f'Kyiv City, the Independence Square {randint(1,38)}, app.{randint(1,12)}'], contact_dictionary, path_file)
   
    if SaveTheBook().save_book(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_add_note(user_command: List[str], book: NoteBook, path_file: str) -> str:
    """"add note ...": The bot create new record note in notebook 
    and save it in file(path_file). Instead of ... the user enters the name for note.

        Parameters:
            user_command (List[str]): List of user command (name of note).
            book (NoteBook): Instance of NoteBook.
            path_file (str): Is there path and filename of notebook.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]

    new_record = Note(name, ' '.join(user_command[2:]))

    book.add_record(new_record)

    if SaveTheBook().save_book(book, path_file):
        return OTHER_MESSAGE.get('successful addition', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_remove_note(user_command: List[str], book: NoteBook, path_file: str) -> str:
    """"remove note...": The bot remove a record note in note-books 
    and save it in file(path_file). Instead of ... the user enters the name for note.

        Parameters:
            user_command (List[str]): List of user command (name of note).
            book (NoteBook): Instance of NoteBook.
            path_file (str): Is there path and filename of notebook.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]

    if book.get(name, None):

        book.remove_record(name)

        if SaveTheBook().save_book(book, path_file):
            return OTHER_MESSAGE.get('deleting successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        return WARNING_MESSAGE.get('unknown note', AMBUSH)


@input_error
def handler_change_note(user_command: List[str], book: NoteBook, path_file: str) -> str:
    """"change note ...": The bot stores the new note of the existing 
    data in NoteBook and save it in file(path_file).
    Instead of ... the user enters the name, tag(s) note and new note text, 
    necessarily with a space.

        Parameters:
            user_command (List[str]): List of user command (name of note).
            book (NoteBook): Instance of NoteBook.
            path_file (str): Is there path and filename of notebook.

        Returns:
            string(str): Answer for the user.
    """
    name = user_command[1]
    
    book[name].change_note()

    if SaveTheBook().save_book(book, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


@input_error
def handler_show_notes(_, book: NoteBook, __) -> list:
    """"show notes": The bot outputs all saved notes from notebook.

        Parameters:
            _: not matter (user_command (List[str]): List of user command).
            book (NoteBook): Instance of NoteBook.
            _a: not matter (path_file (str): Is there path and filename of note book).

        Returns:
            string(str): Answer for the user (list of string of all users).
    """
    all_list = [OTHER_MESSAGE.get('all list', [AMBUSH]*2)[1]]

    for records in book.iterator(LIMIT_RECORDS_TO_DISPLAY):
        volume = ''

        for record in records:

            # volume += forming_note_information(record)
            volume += f'{record.name}; '

        all_list.append(volume)

    return all_list


@input_error
def handler_show_note(user_command: List[str], book: NoteBook, _=None) -> str:
    """"show information about a specific note". With this command, the bot outputs
    all contents from specific note (name, tags, text) to the console.

        Parameters:
            user_command (List[str]): List of user command (name of note).
            book (NoteBook): Instance of NoteBook.
            _: not matter (path_file (str): Is there path and filename of notebook).

        Returns:
            string(str): Answer for the user (string of information about user).
    """
    name = user_command[1]

    return f'{book[name]}'


def handler_sort(user_command: List[str], __=None, _=None) -> str:  # *args ?
    """"sort...": The bot sorts files by category in the specified folder.
        Example:
            sort /home/user/junk

        Parameters:
            user_command (List[str]): List of user command (path for folder).
            __: book (NoteBook): Instance of NoteBook.
            _: path_file (str) - Is there path and filename of notebook.

        Returns:
            result (str): Answer for the user - result of sorting.
    """ 
    return junk_sorter.main(user_command[1])


@input_error
def handler_find_notes(user_command: List[str], book: NoteBook, _=None) -> list:
    """"find notes...": The bot outputs a list of notes whose name or content 
    matches the entered one or more(with an OR setting) string without space(' ').

        Parameters:
            user_command (List[str]): List of user command (string(s) for searching).
            book (NoteBook): Instance of NoteBook.
            _: path_file (str) - Is there path and filename of notebook.

        Returns:
            found_list (list): Answer for the user - list of string of found notes.
    """ 
    found_list = [OTHER_MESSAGE.get('found_notes', [AMBUSH])[0]]
 
    for records in book.iterator(LIMIT_RECORDS_TO_DISPLAY): 
        volume = ''

        for record in records:

            if find_notes(user_command[1:], record):

                volume += f'{book[record.name]}'

        found_list.append(volume)

    return found_list


def handler_sort_notes(__, book: NoteBook, _=None) -> list:
    """"sort notes...": The bot outputs a list of notes whose tags most wanted .

        Parameters:
            __: user_command (List[str]): List of user command (string(s) for searching).
            book (NoteBook): Instance of NoteBook.
            _: path_file (str) - Is there path and filename of notebook.

        Returns:
            found_list (list): Answer for the user - list of string of found notes.
    """ 
    return book.sort_by_tags()


ALL_COMMAND_ADDRESSBOOK = {
    '?': handler_help,
    'add_address': handler_add_address,
    'add_birthday': handler_add_birthday,
    'add_details': handler_add_details,
    'add_email': handler_add_email,
    'add_nickname': handler_add_nickname,
    'add_phone': handler_add_phone,
    'add': handler_add,
    'change_address': handler_change_address,
    'change_birthday': handler_change_birthday,
    'change_details': handler_change_details,
    'change_email': handler_change_email,
    'change': handler_change,
    'close': handler_exit,
    'email': handler_email,
    'exit': handler_exit,
    'find': handler_find,
    'gen': secret_command,
    'good_bye': handler_exit,
    'happy_birthday': handler_happy_birthday,
    'hello': handler_hello,
    'help': handler_help,
    'phone': handler_phone,
    'remmove_address': handler_remove_address,
    'remove_birthday': handler_remove_birthday,
    'remove_details': handler_remove_details,
    'remove_email': handler_remove_email,
    'remove_phone': handler_remove_phone,
    'remove': handler_remove,
    'show_all': handler_show_all,
    'show': handler_show,
    'sort': handler_sort,
    }
ALL_COMMAND_NOTEBOOK = {
    'add_note': handler_add_note,
    'show_notes': handler_show_notes,
    'show_note': handler_show_note,
    'remove_note': handler_remove_note,
    'change_note': handler_change_note,
    'find_notes': handler_find_notes,
    'sort_notes': handler_sort_notes,
}
ALL_COMMAND_FILESORTER = {

}

ALL_COMMAND = {'command_guesser': handler_command_guesser,}
ALL_COMMAND.update(ALL_COMMAND_ADDRESSBOOK)
ALL_COMMAND.update(ALL_COMMAND_NOTEBOOK)
ALL_COMMAND.update(ALL_COMMAND_FILESORTER)

def main_handler(user_command: List[str], contact_dictionary: Union[AddressBook, NoteBook], path_file: str) -> Union[str, list]:
    """All possible bot commands. Get a list of command and options, 
    a dictionary of contacts, and the path to an address book file. 
    Call a certain function and return a response to a command request.

        Parameters:
            user_command (List[str]): list of user command (list of command and options).
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book (in str).

        Returns:
            The result of the corresponding function (list): The result of the\
                 certain function is a string or a list of strings.
    """
    return ALL_COMMAND.get(user_command[0], lambda *args: None)(user_command, contact_dictionary, path_file) \
        or OTHER_MESSAGE.get('Unknown', [AMBUSH])[0]
