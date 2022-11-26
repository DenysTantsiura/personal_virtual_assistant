from typing import List, Union

from .address_book import AddressBook
from .auxiliary_functions import find_users, forming_user_information
from .classes_address_book import Record
from .constant_config import (
    AMBUSH,
    LIMIT_RECORDS_TO_DISPLAY, 
    WARNING_MESSAGE, 
    OTHER_MESSAGE,
)
from .main_validator import input_error
from .serialization import address_book_saver


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

    if address_book_saver(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('successful addition', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


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

        if address_book_saver(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'


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

        if address_book_saver(contact_dictionary, path_file):
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

    if address_book_saver(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


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

    if address_book_saver(contact_dictionary, path_file):
        return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
    else:
        return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)


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

        if address_book_saver(contact_dictionary, path_file):
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

        if address_book_saver(contact_dictionary, path_file):
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

        if address_book_saver(contact_dictionary, path_file):
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

        if address_book_saver(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('update successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
        no_changes = OTHER_MESSAGE.get('no changes', [AMBUSH])[0]
        return f'{no_changes}{verdict[1]}'



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


def handler_hello(*_) -> str:
    """Reply to the greeting."""
    return OTHER_MESSAGE.get('Hello', [AMBUSH])[0]


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

        if address_book_saver(contact_dictionary, path_file):
            return OTHER_MESSAGE.get('deleting successful', [AMBUSH])[0]
        else:
            return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

    else:
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

            if address_book_saver(contact_dictionary, path_file):
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

            if address_book_saver(contact_dictionary, path_file):
                return OTHER_MESSAGE.get('deleting field', [AMBUSH])[0]
            else:
                return WARNING_MESSAGE.get('unsuccessful save', AMBUSH)

        else:
            nickname2 = OTHER_MESSAGE.get('Rnickname', [AMBUSH]*3)[2]
            return f'{nickname2}\"{name}\"'

    else:  # duplicate 'of except TheContactIsNotExist'
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

                if address_book_saver(contact_dictionary, path_file):
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

                if address_book_saver(contact_dictionary, path_file):
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


def handler_exit(*_) -> str:
    """Reply to the exit command."""
    return OTHER_MESSAGE.get('Bye', [AMBUSH])[0]


def handler_help(*_) -> str:
    """
    Return all known commands.
    """
    all_commands_list = [OTHER_MESSAGE.get('all commands list', [AMBUSH])[0]]
    all_commands_list += [f'''{key.replace('_',' ')}\n''' for key in ALL_COMMAND]
    return ''.join(all_commands_list)


ALL_COMMAND = {
    'hello': handler_hello,
    'add': handler_add,
    'add_email': handler_add_email,
    'add_phone': handler_add_phone,
    'add_nickname': handler_add_nickname,
    'change': handler_change,
    'change_email': handler_change_email,
    'email': handler_email,
    'phone': handler_phone,
    'show_all': handler_show_all,
    'good_bye': handler_exit,
    'close': handler_exit,
    'exit': handler_exit,
    'show': handler_show,
    'add_birthday': handler_add_birthday,
    'change_birthday': handler_change_birthday,
    'find': handler_find,
    'remove': handler_remove,
    'remove_email': handler_remove_email,
    'remove_phone': handler_remove_phone,
    'remove_birthday': handler_remove_birthday,
    'help': handler_help,
    '?': handler_help,
    }


def main_handler(user_command: List[str], contact_dictionary: AddressBook, path_file: str) -> Union[str, list]:
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
