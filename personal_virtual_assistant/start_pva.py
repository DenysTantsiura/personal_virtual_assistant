""" rearch...
NEXT NEED more TESTS!  + split to modules and... and next function for new field  ! MAP_ALL
lines 91, 1307, !!!!!!!!!!!!!!!!!!!!!!!!! 

-help for each command (from docstrings?)
-split to modules
-add e-mail commands
-add block in phone and mail commands
-add detail and related... commands
-Cweb2 + video
-описати абстрактний базовий клас для представлень користувача і конкретні реалізації, які наслідують базовий клас і реалізують консольний інтерфейс.
"""
import sys
from typing import NoReturn

from system import *
## or Implicitly necessary import AddressBook:
# from system.command_parser import parser
# from system.constant_config import (
#     AMBUSH,
#     DEFAULT_FILE_ADDRESS_BOOK,
#     WARNING_MESSAGE, 
#     OTHER_MESSAGE,
# )
# from system.handlers import main_handler
# from system.serialization import (
#     helper_try_load_file,
#     helper_try_open_file,
# )


def main() -> NoReturn:
    """The main function of launching a helper console bot that 
    recognize the commands entered from the keyboard and respond 
    according to the command entered.
    Enter a command - get an answer.
    """
    try:
        path_file = sys.argv[1]

    except IndexError:
        path_file = DEFAULT_FILE_ADDRESS_BOOK

    new_path_file = helper_try_open_file(path_file)

    contact_dictionary, new_path_file = helper_try_load_file(new_path_file)

    while True:
        user_command = input(OTHER_MESSAGE.get('START', [AMBUSH])[0])
        user_request = parser(user_command)
        bot_answer = main_handler(
            user_request, contact_dictionary, new_path_file)

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
            break


if __name__ == '__main__':
    main()
