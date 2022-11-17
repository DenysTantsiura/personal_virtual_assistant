

AMBUSH = 'AMBUSH!'
TO_NEXT_FILE_NAME = 'new_one_'
DEFAULT_FILE_ADDRESS_BOOK = 'ABook.data'
LIMIT_RECORDS_TO_DISPLAY = 10 

PREFORMATING_PHONE = r'^\+[0-9)(-]{12,16}$'
PREFORMATING_EMAIL1 = r'\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]{2,}[ ]'
PREFORMATING_EMAIL2 = r'\b[a-zA-z][\w_.]+@[a-zA-z]+\.[a-zA-z]+\.[a-zA-z]{2,}'

ERROR_MESSAGE = {
    'UnpicklingError': ['The File', ' is corrupted, my apologies.', ],
    'UnpicklingOthers': ['Is the File', ' corrupted? ', ],
    'OpenFile': ['No access to File', ', system error: ', ],
    'WriteFile': ['No access to write File', ', error: ', ],
    'PicklingError': ['Can\'t save object in file', ', my apologies.', ],
    'PicklingOthers': ['Something was wrong. File', ' is not updated. ', ],
    'UnknownCommand': ['Unknown command ...', ],
    'UnpredictableError': ['Unpredictable error: No contact record available?...', ],
    'UnexpectedError': ['Unexpected error!: ', ],
    '': ['', ],
    '': ['', ],
    '': ['', ],
}

WARNING_MESSAGE = {
    'name': 'At the beginning there can be only a Latin letter!',
    'birthday': 'Incorrect or nonexistent date, entry must be in year-month-day format (YYYY-MM-DD).',
    'phone': 'The number is obviously incorrect, the value should start with \"+\" and have 12 digits.',
    'email': 'The e-mail is obviously incorrect.',
    'main': 'Something happened. Will you try again?',
    'name is omitted': 'Give me name OR name and phone please.\n',
    'the contact exists': 'Such an entry is already in the book. Add or change a number.',
    'invalid name': 'A name cannot begin with a number and can only begin with Latin characters!\n',
    'invalid phone': '''There are no valid phone numbers.
    The number must be in the following format with 12 digits(d):
    +dd(ddd)ddd-dddd .\n''',
    'empty record to add': 'There were no new entries to add.\n',
    'unsuccessful save': 'Failed to save file.',
    'name and phone omitted': 'Give me name and new phone(s) please.\n',
    'unknown name': 'The user is unknown. There are no records for this name yet. Create it first.',
    'no address book': 'No contact records available.\n',
    'name and birthday omitted': 'Give me a name and birthday, please.\n',
    'invalid birthday entry': 'The year of birth is not correct! A person too old or too young.\n',
    'invalid birthday': 'The calendar date is not possible!\n',
    'name and 2 phones omitted': 'Give me name and 2 phones please (current and new)\n',
    'no search query': 'There is no search query\n',
    'name is missing': 'Give me a name too, please.\n',
    '': '',
    '': '',
}

OTHER_MESSAGE = {
    'Record': ['\n\nRecord(Name: ', '; Phones: ', '; Birthday: ', ';\n\te-mail: ', ';\n\t details: ', \
               ':\n\t related information: ', ],
    'RBirthday': ['Birthday already recorded for ', '. You can change it.', 'Birthday not specified for ', \
                  '. You can add it.', ],
    'RPhone': [' already recorded for ', 'No phone(s) entry in record ', ' not specified in the contact ', ],
    'ABook': ['AddressBook(Records:', ],
    'next_page': ['Press Enter for next Volume... ', ],
    'Bye': ['Good bye!', ],
    'START': ['Can I help you?\n', ],
    'Unknown': ['It is unclear. Unknown command...', ],
    'Hello': ['Hello! So...\n', ],
    'successful addition': ['A record(s) have been added.\n', ],
    'update successful': ['A record have been added. Address book file has been saved.', ],
    'no changes': ['No changes have been made.\n', ],
    'deleting successful': ['Record successfully deleted. Results saved.', ],
    'deleting field': ['Field record deleted successfully. Results saved.', ],
    'no new entries': ['There were no entries to add.\n', ],
    'found': ['Entries found in your contact book:', ', birthday: ', '(days to next birthday: ', '. Will be ', \
              ' yrs. old)\n-> phone(s): ', ', birthday: unknown\n-> phone(s): ', ],
    'all list': ['Entries in your contact book:', ],
    'all commands list': ['All commands in current version Personal Virtual Assistant:\n', \
                          'Detailed for each command: \"-h\" after them.\n', ],  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
    '': ['', ],
    '': ['', ],
}
