from datetime import datetime
import re

from .address_book import AddressBook
from .constant_config import (
    AMBUSH,
    BIRTHDAY_FORMAT,
    PREFORMATTING_EMAIL1,
    PREFORMATTING_EMAIL2, 
    PREFORMATTING_PHONE,
    WARNING_MESSAGE, 
)
from .except_classes import (
    AnIllogicalLimit,
    InvalidBirthday,
    InvalidBirthdayEntry,
    NoAddressBook,
    NoSearchQuery,
    TheContactIsExist,
    TheContactIsNotExist,
    TheDetailsIsMissing,
    TheEmailIsIncorrect,
    TheNameAnd2EmailsAreMissing,
    TheNameAnd2PhonesAreMissing,
    TheNameAndAddressAreMissing,
    TheNameAndBirthdayAreMissing,
    TheNameAndEmailAreMissing,
    TheNameAndNicknameAreMissing,
    TheNameAndPhoneAreMissing,
    TheNameIsIncorrect,
    TheNameIsMissing,
    TheNameIsOmitted,
    ThePhoneIsIncorrect,
    NoEndDay,
    NoNoteBook,
    TheNoteNameIsMissing,
    TheNoteDuplicate,
)
from .note_book import NoteBook


def validation_add_details(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not name:  # len(user_command) < 3:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    if len(user_command) < 4:
        raise TheDetailsIsMissing


def validation_add_email(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if len(user_command) < 3:  # or not name:
        raise TheNameAndEmailAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    email_count = 0

    for email_candidate in user_command[2:]:
        email_matches = re.search(PREFORMATTING_EMAIL1, email_candidate) or\
             re.search(PREFORMATTING_EMAIL2, email_candidate)
        
        if email_matches:
            email_count += 1

        else:
            print(f'{email_candidate}', WARNING_MESSAGE.get('email', AMBUSH))

    if email_count < len(user_command[2:]):  # not email_count:
        raise TheEmailIsIncorrect


def validation_add_phone(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if len(user_command) < 3:  # or not name:
        raise TheNameAndPhoneAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    phone_count = 0

    for phone_candidate in user_command[2:]:
        phone_matches = re.search(PREFORMATTING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < len(user_command[2:]):  # not phone_count:
        raise ThePhoneIsIncorrect


def validation_add(user_command: list, contact_dictionary: AddressBook) ->\
        None:
    """Check the input parameters. Raise a mismatch exception if found."""
    name = user_command[1] if len(user_command) > 1 else None

    if not name:  # len(user_command) < 2:
        raise TheNameIsOmitted

    if name in contact_dictionary:
        raise TheContactIsExist

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if len(user_command) >= 2:
        phone_count = 0

        for phone_candidate in user_command[2:]:
            phone_matches = re.search(PREFORMATTING_PHONE, phone_candidate)

            if phone_matches:
                phone_count += 1

            else:
                print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

        if phone_count < len(user_command[2:]):  # not phone_count:
            raise ThePhoneIsIncorrect


def validation_address(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Raise exception if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook 

    if len(user_command) < 3:  # or not name:
        raise TheNameAndAddressAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_birthday(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Raise exception if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook 

    if len(user_command) < 3:  # or not name:
        raise TheNameAndBirthdayAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if datetime.now().year - 122 > int(user_command[2].split('-')[0]) > datetime.now().year - 8:  # 0, 8, 14, 16, 18 ?
        raise InvalidBirthdayEntry

    else:
        try:
            datetime.strptime(user_command[2], BIRTHDAY_FORMAT)

        except ValueError:
            raise InvalidBirthday


def validation_change_details(user_command: list, contact_dictionary: AddressBook) -> \
        None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 3:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    if len(user_command) < 4:
        raise TheDetailsIsMissing


def validation_change_email(user_command: list, contact_dictionary: AddressBook) -> \
        None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if len(user_command) < 4:  # or not name:
        raise TheNameAnd2EmailsAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    email_count = 0

    for email_candidate in user_command[2:]:
        email_matches = re.search(PREFORMATTING_EMAIL1, email_candidate) or\
             re.search(PREFORMATTING_EMAIL2, email_candidate)
        
        if email_matches:
            email_count += 1

        else:
            print(f'{email_candidate}', WARNING_MESSAGE.get('email', AMBUSH))

    if email_count < len(user_command[2:]):  # not email_count:
        raise TheEmailIsIncorrect


def validation_change(user_command: list, contact_dictionary: AddressBook) -> \
        None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if len(user_command) < 4:  # or not name:
        raise TheNameAnd2PhonesAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    phone_count = 0

    for phone_candidate in user_command[2:]:
        phone_matches = re.search(PREFORMATTING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < len(user_command[2:]):  # not phone_count:
        raise ThePhoneIsIncorrect


def validation_email(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 2 or not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_find(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    query = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not query:
        raise NoSearchQuery


def validation_happy_birthday(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    end_day = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not end_day:
        raise NoEndDay
    
    if 1 > int(end_day) > 90:
        raise AnIllogicalLimit


def validation_nickname(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Raise exception if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook 

    if len(user_command) < 3:  # or not name:
        raise TheNameAndNicknameAreMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_phone(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 2 or not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_remove_address(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 2:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist


def validation_remove_birthday(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 2:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist


def validation_remove_details(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:  # len(user_command) < 2:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist


def validation_remove_email(user_command: list, contact_dictionary: AddressBook) -> \
        None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    email_count = 0

    for email_candidate in user_command[2:]:
        email_matches = re.search(PREFORMATTING_EMAIL1, email_candidate) or\
             re.search(PREFORMATTING_EMAIL2, email_candidate)
        
        if email_matches:
            email_count += 1

        else:
            print(f'{email_candidate}', WARNING_MESSAGE.get('email', AMBUSH))

    if email_count < 2:  # len(user_command[2:])  # not email_count:
        raise TheEmailIsIncorrect


def validation_remove_phone(user_command: list, contact_dictionary: AddressBook) -> \
        None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist

    phone_count = 0

    for phone_candidate in user_command[2:]:
        phone_matches = re.search(PREFORMATTING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < 2:  # len(user_command[2:])  # not phone_count:
        raise ThePhoneIsIncorrect


def validation_remove(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect

    if name not in contact_dictionary:
        raise TheContactIsNotExist


def validation_show_all(_, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    if not contact_dictionary:
        raise NoAddressBook


def validation_show(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_add_note(user_command: list, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not name:
        raise TheNoteNameIsMissing
    
    if book.get(name, None):
        raise TheNoteDuplicate

def validation_remove_note(user_command: list, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not book:
        raise NoNoteBook

    if not name:
        raise TheNoteNameIsMissing


def validation_change_note(user_command: list, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not book:
        raise NoNoteBook

    if not name:
        raise TheNoteNameIsMissing


def validation_show_notes(_, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""

    if not book:
        raise NoNoteBook


def validation_show_note(user_command: list, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not book:
        raise NoNoteBook

    if not name:
        raise TheNoteNameIsMissing


def validation_find_notes(user_command: list, book: NoteBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    query = user_command[1] if len(user_command) > 1 else None

    if not book:
        raise NoNoteBook

    if not query:
        raise NoSearchQuery


VALIDATION_FUNCTIONS = {
            'handler_add_address': validation_address,
            'handler_add_birthday': validation_birthday,
            'handler_add_details': validation_add_details,
            'handler_add_email': validation_add_email,
            'handler_add_nickname': validation_nickname,
            'handler_add_phone': validation_add_phone,
            'handler_add': validation_add,
            'handler_change_address': validation_address,
            'handler_change_birthday': validation_birthday,
            'handler_change_details': validation_change_details,
            'handler_change_email': validation_change_email,
            'handler_change_nickname': validation_nickname,
            'handler_change': validation_change,
            'handler_email': validation_email,
            'handler_find': validation_find,
            'handler_happy_birthday': validation_happy_birthday,
            'handler_phone': validation_phone,
            'handler_remove_address': validation_remove_address,
            'handler_remove_birthday': validation_remove_birthday,
            'handler_remove_details': validation_remove_details,
            'handler_remove_email': validation_remove_email,
            'handler_remove_nickname': validation_nickname,
            'handler_remove_phone': validation_remove_phone,
            'handler_remove': validation_remove,
            'handler_show_all': validation_show_all,
            'handler_show': validation_show,
            'handler_add_note': validation_add_note,
            'handler_remove_note': validation_remove_note,
            'handler_change_note': validation_change_note,
            'handler_show_notes': validation_show_notes,
            'handler_show_note': validation_show_note,
            'handler_find_notes': validation_find_notes,
            # 'unknown': lambda *_: raise UnknownCommand,  # 'Unknown command...'
        }
