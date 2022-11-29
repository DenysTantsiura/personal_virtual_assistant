import os
import pickle

from .address_book import AddressBook
from .constant_config import (
    AMBUSH, 
    ERROR_MESSAGE, 
    TO_NEXT_FILE_NAME,
)


def address_book_saver(contact_dictionary: AddressBook, path_file: str) -> bool:
    """Save a class AddressBook to a file (path_file).

        Parameters:
            contact_dictionary (AddressBook): Instance of AddressBook.
            path_file (str): Is there path and filename of address book.

        Returns:
            File save success marker (bool).
    """
    try:

        with open(path_file, 'wb') as db_file:

            try:

                pickle.dump(contact_dictionary, db_file)

            except pickle.PicklingError:
                error_save0 = ERROR_MESSAGE.get('PicklingError', [AMBUSH])[0]
                error_save1 = ERROR_MESSAGE.get('PicklingError', [AMBUSH]*2)[1]
                print(f'{error_save0}({path_file}){error_save1}')
                return False
                # contact_dictionary = AddressBook()

            except Exception as error_:  # pickle.PickleError inherits Exception.
                error_save0 = ERROR_MESSAGE.get('PicklingOthers', [AMBUSH])[0]
                error_save1 = ERROR_MESSAGE.get('PicklingOthers', [AMBUSH]*2)[1]
                print(f'{error_save0}({path_file}){error_save1}\n{repr(error_)}')
                return False
                # contact_dictionary = AddressBook()

    except OSError as error_:
        error_write0 = ERROR_MESSAGE.get('WriteFile', [AMBUSH])[0]
        error_write1 = ERROR_MESSAGE.get('WriteFile', [AMBUSH]*2)[1]
        print(f'{error_write0}({path_file}){error_write1}\n{type(error_)}: {error_}')
        return False

    except Exception as error_:
        error_write0 = ERROR_MESSAGE.get('WriteFile', [AMBUSH])[0]
        error_write1 = ERROR_MESSAGE.get('WriteFile', [AMBUSH]*2)[1]
        print(f'{error_write0}({path_file}){error_write1}\n{repr(error_)}')
        return False

    return True


def helper_try_load_file(path_file: str) -> tuple[AddressBook, str]:
    """Create empty address book (AddressBook) if no file on path_file.
    Or, try to load address book database (read) from file. 
    Return loaded address book (AddressBook) and path for address book file.

        Parameters:
            path_file (str): Is existed file (name or name with path).

        Returns:
            contact_dictionary (AddressBook): Loaded from file or new empty class.
            path_file (str): The file name to save the address book in the following steps.
                Unoccupied name of file, if an exception occurred.
    """
    if not os.path.exists(path_file):
        contact_dictionary = AddressBook()
        address_book_saver(contact_dictionary, path_file)  # False (= If can't save file!)
        return contact_dictionary, path_file

    try:
        with open(path_file, 'rb') as fh:
            try:
                contact_dictionary = pickle.load(fh)
                return contact_dictionary, path_file
            except pickle.UnpicklingError:
                error_load0 = ERROR_MESSAGE.get('UnpicklingError', [AMBUSH])[0]
                error_load1 = ERROR_MESSAGE.get('UnpicklingError', [AMBUSH]*2)[1]
                print(f'{error_load0}({path_file}){error_load1}')
                contact_dictionary = AddressBook()

            except Exception as error_:  # pickle.PickleError inherits Exception.
                error_load0 = ERROR_MESSAGE.get('UnpicklingOthers', [AMBUSH])[0]
                error_load1 = ERROR_MESSAGE.get('UnpicklingOthers', [AMBUSH]*2)[1]
                print(f'{error_load0}({path_file}){error_load1}\n{repr(error_)}')
                contact_dictionary = AddressBook()

    except OSError as error_:
        error_load0 = ERROR_MESSAGE.get('OpenFile', [AMBUSH])[0]
        error_load1 = ERROR_MESSAGE.get('OpenFile', [AMBUSH]*2)[1]
        print(f'{error_load0}({path_file}){error_load1}\n{type(error_)}: {error_}')
        contact_dictionary = AddressBook()

    except Exception as error_:
        error_load0 = ERROR_MESSAGE.get('OpenFile', [AMBUSH])[0]
        error_load1 = ERROR_MESSAGE.get('OpenFile', [AMBUSH]*2)[1]
        print(f'{error_load0}({path_file}){error_load1}\n{repr(error_)}')
        contact_dictionary = AddressBook()

    while os.path.exists(path_file):
        path_file = os.path.join(os.path.dirname(path_file), TO_NEXT_FILE_NAME + os.path.basename(path_file))

    return contact_dictionary, path_file


def helper_try_open_file(path_file: str) -> str:
    """Checks if the database file exists and checks if the filename is free if not.
    If exist folder with path_file file name, then return new free file name. 
    Return unoccupied name of file (string).

        Parameters:
            path_file (str): Is proposed name of file.

        Returns:
            path_file (str): Unoccupied name of file.
    """
    if os.path.isdir(path_file):

        while os.path.isdir(path_file):

            path_file = os.path.join(os.path.dirname(path_file), TO_NEXT_FILE_NAME + os.path.basename(path_file))

    return path_file
