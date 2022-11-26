from datetime import datetime
import re

from .address_book import AddressBook
from .constant_config import (
    AMBUSH,
    BIRTHDAY_FORMAT,
    PREFORMATING_PHONE,
    PREFORMATING_EMAIL1,
    PREFORMATING_EMAIL2, 
    WARNING_MESSAGE, 
)
from .except_classes import (
    TheNameIsOmitted,  # alphabetical?
    TheContactIsExist,
    TheNameIsIncorrect,
    TheEmailIsIncorrect,
    ThePhoneIsIncorrect,
    TheNameAndEmailAreMissing,
    TheNameAndPhoneAreMissing,
    TheContactIsNotExist,
    NoAddressBook,
    TheNameAndBirthdayAreMissing,
    TheNameAndNicknameAreMissing,
    InvalidBirthdayEntry,
    InvalidBirthday,
    TheNameAnd2EmailsAreMissing,
    TheNameAnd2PhonesAreMissing,
    NoSearchQuery,
    TheNameIsMissing,
)


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
            phone_matches = re.search(PREFORMATING_PHONE, phone_candidate)

            if phone_matches:
                phone_count += 1

            else:
                print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

        if phone_count < len(user_command[2:]):  # not phone_count:
            raise ThePhoneIsIncorrect


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
        email_matches = re.search(PREFORMATING_EMAIL1, email_candidate) or\
             re.search(PREFORMATING_EMAIL2, email_candidate)
        
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
        phone_matches = re.search(PREFORMATING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < len(user_command[2:]):  # not phone_count:
        raise ThePhoneIsIncorrect


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
        phone_matches = re.search(PREFORMATING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < len(user_command[2:]):  # not phone_count:
        raise ThePhoneIsIncorrect


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
        email_matches = re.search(PREFORMATING_EMAIL1, email_candidate) or\
             re.search(PREFORMATING_EMAIL2, email_candidate)
        
        if email_matches:
            email_count += 1

        else:
            print(f'{email_candidate}', WARNING_MESSAGE.get('email', AMBUSH))

    if email_count < len(user_command[2:]):  # not email_count:
        raise TheEmailIsIncorrect


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
        email_matches = re.search(PREFORMATING_EMAIL1, email_candidate) or\
             re.search(PREFORMATING_EMAIL2, email_candidate)
        
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
        phone_matches = re.search(PREFORMATING_PHONE, phone_candidate)
        
        if phone_matches:
            phone_count += 1

        else:
            print(f'{phone_candidate}', WARNING_MESSAGE.get('phone', AMBUSH))

    if phone_count < 2:  # len(user_command[2:])  # not phone_count:
        raise ThePhoneIsIncorrect


def validation_show(user_command: list, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    name = user_command[1] if len(user_command) > 1 else None

    if not contact_dictionary:
        raise NoAddressBook

    if not name:
        raise TheNameIsMissing

    if name[0].isdigit() or not name[0].isalpha():
        raise TheNameIsIncorrect


def validation_show_all(_, contact_dictionary: AddressBook) -> None:
    """Check the input parameters. Return a message (str) about a discrepancy if it is detected."""
    if not contact_dictionary:
        raise NoAddressBook


VALIDATION_FUNCTIONS = {
            'handler_add': validation_add,
            'handler_add_birthday': validation_birthday,
            'handler_add_nickname': validation_nickname,
            'handler_add_email': validation_add_email,
            'handler_add_phone': validation_add_phone,
            'handler_change': validation_change,
            'handler_change_email': validation_change_email,
            'handler_change_birthday': validation_birthday,
            'handler_change_nickname': validation_nickname,
            'handler_find': validation_find,
            'handler_email': validation_email,
            'handler_phone': validation_phone,
            'handler_remove': validation_remove,
            'handler_remove_birthday': validation_remove_birthday,
            'handler_remove_nickname': validation_nickname,
            'handler_remove_email': validation_remove_email,
            'handler_remove_phone': validation_remove_phone,
            'handler_show': validation_show,
            'handler_show_all': validation_show_all,
            # 'unknown': lambda *_: raise UnknownCommand,  # 'Unknown command...'
        }
