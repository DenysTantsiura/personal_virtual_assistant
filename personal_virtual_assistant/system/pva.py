from abc import ABC, abstractmethod
import sys
from typing import NoReturn, Union


from .address_book import AddressBook
from .handlers import (
    main_handler,
    ALL_COMMAND_ADDRESSBOOK,
    ALL_COMMAND_NOTEBOOK,
    ALL_COMMAND_FILESORTER,
)
from .command_parser import parser
from .constant_config import (
    AMBUSH, 
    DEFAULT_FILE_ADDRESS_BOOK, 
    OTHER_MESSAGE, 
    WARNING_MESSAGE, 
    DEFAULT_FILE_NOTE_BOOK, 
)
from .note_book import NoteBook
from .serialization import LoadBook, OpenBook


class InterfaceInput(ABC):

    @abstractmethod
    def listen(self, *args, **kwargs):
        ...


class InterfaceOutput(ABC):

    @abstractmethod
    def show_out(self, *args, **kwargs):
        ...


class InputToParser(InterfaceInput):

    def listen(self, request=OTHER_MESSAGE.get('START', [AMBUSH])[0]):
        return parser(input(request))


class OutputAnswer(InterfaceOutput):

    def show_out(self, user_request: list, book_instance: Union[AddressBook, NoteBook], new_path_file: str) -> bool:

        bot_answer = main_handler(user_request, book_instance, new_path_file)

        if isinstance(bot_answer, str):
            
            print(bot_answer)

        elif isinstance(bot_answer, list):

            for volume in bot_answer:

                if volume:

                    print(volume)
                    input(OTHER_MESSAGE.get('next_page', [AMBUSH])[0])

        else:
            print(WARNING_MESSAGE.get('main', AMBUSH))

        if bot_answer == OTHER_MESSAGE.get('Bye', [AMBUSH])[0]:
            return False 

        return True


class PVA:

    def __init__(self) -> None:

        try:
            self.path_file = sys.argv[1]

        except IndexError:
            self.path_file = DEFAULT_FILE_ADDRESS_BOOK
        
        try:
            self.path_file_notes = sys.argv[2]

        except IndexError:
            self.path_file_notes = DEFAULT_FILE_NOTE_BOOK

        self.path_file = OpenBook(self.path_file).open_book()
        self.path_file_notes = OpenBook(self.path_file_notes).open_book()

        self.contact_dictionary, self.path_file = LoadBook(self.path_file).load_book()
        self.note_book, self.path_file_notes = LoadBook(self.path_file_notes).load_book(NoteBook)

    def start(self) -> NoReturn:
        """The main function of launching a helper console bot that 
        recognize the commands entered from the keyboard and respond 
        according to the command entered.
        Enter a command - get an answer.
        """
        while True:

            user_request = InputToParser().listen()
            # print(f'...user_request... is\n{user_request}\n...\n')
            if user_request[0] in ALL_COMMAND_ADDRESSBOOK:
                bot_answer_result = OutputAnswer().show_out(user_request, self.contact_dictionary, self.path_file)
            elif user_request[0] in ALL_COMMAND_NOTEBOOK:
                bot_answer_result = OutputAnswer().show_out(user_request, self.note_book, self.path_file_notes)
            elif user_request[0] in ALL_COMMAND_FILESORTER:
                bot_answer_result = OutputAnswer().show_out(user_request, None, '')
            else:
                # bot_answer_result = OutputAnswer().show_out(user_request, self.contact_dictionary, self.path_file)
                user_request = ['command_guesser'] + user_request
                bot_answer_result = OutputAnswer().show_out(user_request, None, '')

            if not bot_answer_result:
                break
