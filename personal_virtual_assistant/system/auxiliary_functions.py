from typing import List

from .classes_address_book import Record
from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE,
)


def find_users(search_strings: List[str], record: Record) -> bool:
    """Check a record for matching the search strings.

        Parameters:
            search_strings (List[str]): The data in the list rows in the user's search query.
            record (Record): Record - User account card.

        Returns:
            True or False (bool): Search result (Search success rate).
    """
    name = f'{record.name}'

    for search_string in search_strings:

        if name.find(search_string) >= 0:

            return True

        if record.birthday:

            birthday = f'{record.birthday}'

            if birthday.find(search_string) >= 0:

                return True

        for phone in record.phones:
            candidate = f"{phone.value}"
            candidate = candidate.replace(
                '-', '').replace('+', '').replace('(', '').replace(')', '')

            if candidate.find(search_string.replace('-', '').replace('+', '').replace('(', '').replace(')', '')) >= 0:

                return True

    return False


def forming_user_information(record: Record) -> str:
    """Forming user information from a record and returning it as a string.

        Parameters:
            record (Record): User record from the address book.
 
        Returns:
            volume (str): Formed information about the user from record.
    """
    volume = ''
    found_p1 = OTHER_MESSAGE.get('found', [AMBUSH])[1]
    found_p2 = OTHER_MESSAGE.get('found', [AMBUSH])[2]
    found_p3 = OTHER_MESSAGE.get('found', [AMBUSH])[3]
    found_p4 = OTHER_MESSAGE.get('found', [AMBUSH])[4]
    found_p5 = OTHER_MESSAGE.get('found', [AMBUSH])[5]

    if record.birthday:
        volume += f'\n\n{record.name}{found_p1}{record.birthday}' \
            f'{found_p2}{record.days_to_birthday()}'\
            f'{found_p3}{record.years_old()}{found_p4}'

    else:
        volume += f'\n\n{record.name}{found_p5}'
    
    for phone in record.phones:
        volume += f'{phone.value}; '

    return volume
