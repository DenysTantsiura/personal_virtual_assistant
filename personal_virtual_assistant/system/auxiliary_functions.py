from typing import List

from .classes_address_book import Record
from .class_note import Note
from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE,
)


def find_notes(search_strings: List[str], record: Note) -> bool:
    """Check a record for matching the search strings.

        Parameters:
            search_strings (List[str]): The data in the list rows in the user's search query.
            record (Note): Record - Note.

        Returns:
            True or False (bool): Search result (Search success rate).
    """
    content = f'''{record.name} {' '.join(record.tags)} {record.text}'''

    for search_string in search_strings:

        if content.find(search_string) >= 0:

            return True

    return False


def find_users(search_strings: List[str], record: Record) -> bool:
    """Check a record for matching the search strings.

        Parameters:
            search_strings (List[str]): The data in the list rows in the user's search query.
            record (Record): Record - User account card.

        Returns:
            True or False (bool): Search result (Search success rate).
    """
    for search_string in search_strings:

        if forming_user_information(record).find(search_string) >= 0:

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
    found_p1 = OTHER_MESSAGE.get('found', [AMBUSH]*2)[1]
    found_p2 = OTHER_MESSAGE.get('found', [AMBUSH]*3)[2]
    found_p3 = OTHER_MESSAGE.get('found', [AMBUSH]*4)[3]
    found_p4 = OTHER_MESSAGE.get('found', [AMBUSH]*5)[4]
    found_p5 = OTHER_MESSAGE.get('found', [AMBUSH]*6)[5]
    found_p6 = OTHER_MESSAGE.get('found', [AMBUSH]*7)[6]
    found_p7 = OTHER_MESSAGE.get('found', [AMBUSH]*8)[7]
    found_p8 = OTHER_MESSAGE.get('found', [AMBUSH]*9)[8]

    volume += f'\n\n{record.name}'
    if record.name.nickname:
        volume += f'\t({record.name.nickname})'   

    if record.birthday:
        volume += f'{found_p1}{record.birthday}' \
            f'{found_p2}{record.days_to_birthday()}'\
            f'{found_p3}{record.years_old()}{found_p4}'
    
    if record.phones:
        volume += f'{found_p5}'
        for phone in record.phones:
            volume += f'{phone.value}; '
    
    if record.emails:
        volume += f'{found_p6}'
        for email in record.emails:
            volume += f'{email.value}; '

    if record.address:
        volume += f'{found_p7}'
        volume += f'\n{record.address}\n'

    if record.details:
        volume += f'{found_p8}'
        volume += f'\n{record.details}\n'

    return volume
