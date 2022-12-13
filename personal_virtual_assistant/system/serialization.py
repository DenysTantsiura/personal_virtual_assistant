from abc import ABC, abstractmethod
import os
import pickle
from typing import Union

from .address_book import AddressBook
from .constant_config import (
    AMBUSH, 
    ERROR_MESSAGE, 
    TO_NEXT_FILE_NAME,
)
from .note_book import NoteBook   


class CheckingFile(ABC):

    @abstractmethod
    def open_book(self, *args, **kwargs):
        ...

 
class FileSaver(ABC):

    @abstractmethod
    def save_book(self, *args, **kwargs):
        ...       


class LoadFromFile(ABC):

    @abstractmethod
    def load_book(self, *args, **kwargs):
        ...


class LoadBook(LoadFromFile):
    
    def __init__(self, path_file: str) -> None:
        self.path_file = path_file
        
    def load_book(self, book=AddressBook) -> tuple[Union[AddressBook, NoteBook], str]:
        """Create empty book (AddressBook|NoteBook) if no file on path_file.
        Or, try to load book database (read) from file. 
        Return loaded book (AddressBook|NoteBook) and path for address book file.

            Parameters:
                self.path_file (str): Is existed file (name or name with path).
                book (AddressBook|NoteBook): Is class of book type.

            Returns:
                book_instance (AddressBook|NoteBook): Loaded from file or new empty class.
                self.path_file (str): The file name to save the book in the following steps.
                    Unoccupied name of file, if an exception occurred.
        """
        if not os.path.exists(self.path_file):
            book_instance = book()
            SaveTheBook().save_book(book_instance, self.path_file)  # False (= If can't save file!)
            return book_instance, self.path_file

        try:
            with open(self.path_file, 'rb') as fh:
                try:
                    book_instance = pickle.load(fh)
                    return book_instance, self.path_file
                except pickle.UnpicklingError:
                    error_load0 = ERROR_MESSAGE.get('UnpicklingError', [AMBUSH])[0]
                    error_load1 = ERROR_MESSAGE.get('UnpicklingError', [AMBUSH]*2)[1]
                    print(f'{error_load0}({self.path_file}){error_load1}')
                    book_instance = book()

                except Exception as error_:  # pickle.PickleError inherits Exception.
                    error_load0 = ERROR_MESSAGE.get('UnpicklingOthers', [AMBUSH])[0]
                    error_load1 = ERROR_MESSAGE.get('UnpicklingOthers', [AMBUSH]*2)[1]
                    print(f'{error_load0}({self.path_file}){error_load1}\n{repr(error_)}')
                    book_instance = book()

        except OSError as error_:
            error_load0 = ERROR_MESSAGE.get('OpenFile', [AMBUSH])[0]
            error_load1 = ERROR_MESSAGE.get('OpenFile', [AMBUSH]*2)[1]
            print(f'{error_load0}({self.path_file}){error_load1}\n{type(error_)}: {error_}')
            book_instance = book()

        except Exception as error_:
            error_load0 = ERROR_MESSAGE.get('OpenFile', [AMBUSH])[0]
            error_load1 = ERROR_MESSAGE.get('OpenFile', [AMBUSH]*2)[1]
            print(f'{error_load0}({self.path_file}){error_load1}\n{repr(error_)}')
            book_instance = book()

        while os.path.exists(self.path_file):
            self.path_file = os.path.join(os.path.dirname(self.path_file), TO_NEXT_FILE_NAME + os.path.basename(self.path_file))

        return book_instance, self.path_file


class OpenBook(CheckingFile):

    def __init__(self, path_file: str) -> None:
        self.path_file = path_file

    def open_book(self) -> str:
        """Checks if the database file exists and checks if the filename is free if not.
        If exist folder with path_file file name, then return new free file name. 
        Return unoccupied name of file (string).

            Parameters:
                path_file (str): Is proposed name of file.

            Returns:
                path_file (str): Unoccupied name of file.
        """
        if os.path.isdir(self.path_file):

            while os.path.isdir(self.path_file):

                self.path_file = os.path.join(os.path.dirname(self.path_file), TO_NEXT_FILE_NAME + os.path.basename(self.path_file))

        return self.path_file


class SaveTheBook(FileSaver):

    @staticmethod
    def save_book(book_instance: Union[AddressBook, NoteBook], path_file: str) -> bool:
        """Save a class AddressBook|NoteBook to a file (path_file).

            Parameters:
                book_instance (AddressBook|NoteBook): Instance of AddressBook|NoteBook.
                path_file (str): Is there path and filename of book.

            Returns:
                File save success marker (bool).
        """
        try:

            with open(path_file, 'wb') as db_file:

                try:

                    pickle.dump(book_instance, db_file)

                except pickle.PicklingError:
                    error_save0 = ERROR_MESSAGE.get('PicklingError', [AMBUSH])[0]
                    error_save1 = ERROR_MESSAGE.get('PicklingError', [AMBUSH]*2)[1]
                    print(f'{error_save0}({path_file}){error_save1}')
                    return False

                except Exception as error_:  # pickle.PickleError inherits Exception.
                    error_save0 = ERROR_MESSAGE.get('PicklingOthers', [AMBUSH])[0]
                    error_save1 = ERROR_MESSAGE.get('PicklingOthers', [AMBUSH]*2)[1]
                    print(f'{error_save0}({path_file}){error_save1}\n{repr(error_)}')
                    return False

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
