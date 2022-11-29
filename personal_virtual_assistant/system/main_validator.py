from typing import Union

from .address_book import AddressBook
from .constant_config import (
    AMBUSH,  
    ERROR_MESSAGE, 
    WARNING_MESSAGE, 
)
from .except_classes import (
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
    TheNameAndBirthdayAreMissing,
    TheNameAndEmailAreMissing,
    TheNameAndNicknameAreMissing,
    TheNameAndPhoneAreMissing,
    TheNameIsIncorrect,
    TheNameIsMissing,
    TheNameIsOmitted,
    ThePhoneIsIncorrect,
)
from .validators import VALIDATION_FUNCTIONS


def input_error(handler):
    """User error handler (decorator).

        Parameters:
            handler (function): Incoming function.

        Returns:
            exception_function(function): Exception function for handler functions.

    """
    def exception_function(user_command: list, contact_dictionary: AddressBook, path_file: str) -> Union[str, list]:
        """Exception function for handler functions."""
        try:
            VALIDATION_FUNCTIONS[handler.__name__](user_command, contact_dictionary)

        except InvalidBirthday:
            return WARNING_MESSAGE.get('invalid birthday', AMBUSH)
        
        except InvalidBirthdayEntry:
            return WARNING_MESSAGE.get('invalid birthday entry', AMBUSH)

        except KeyError:
            return ERROR_MESSAGE.get('UnknownCommand', AMBUSH)

        except NoAddressBook:
            return WARNING_MESSAGE.get('no address book', AMBUSH)

        except NoSearchQuery:
            return WARNING_MESSAGE.get('no search query', AMBUSH)
        
        except TheContactIsExist:
            return WARNING_MESSAGE.get('the contact exists', AMBUSH)

        except TheContactIsNotExist:
            return WARNING_MESSAGE.get('unknown name', AMBUSH)

        except TheDetailsIsMissing:
            return WARNING_MESSAGE.get('details is missing', AMBUSH)

        except TheEmailIsIncorrect:
            return WARNING_MESSAGE.get('invalid email', AMBUSH)

        except TheNameAnd2EmailsAreMissing:
            return WARNING_MESSAGE.get('name and 2 emails omitted', AMBUSH)

        except TheNameAnd2PhonesAreMissing:
            return WARNING_MESSAGE.get('name and 2 phones omitted', AMBUSH)

        except TheNameAndBirthdayAreMissing:
            return WARNING_MESSAGE.get('name and birthday omitted', AMBUSH)
        
        except TheNameAndEmailAreMissing:
            return WARNING_MESSAGE.get('name and email omitted', AMBUSH)    
        
        except TheNameAndNicknameAreMissing:
            return WARNING_MESSAGE.get('nickname is omitted', AMBUSH)

        except TheNameAndPhoneAreMissing:
            return WARNING_MESSAGE.get('name and phone omitted', AMBUSH)
        
        except TheNameIsIncorrect:
            return WARNING_MESSAGE.get('invalid name', AMBUSH)

        except TheNameIsMissing:
            return WARNING_MESSAGE.get('name is missing', AMBUSH)

        except TheNameIsOmitted:
            return WARNING_MESSAGE.get('name is omitted', AMBUSH)

        except ThePhoneIsIncorrect:
            return WARNING_MESSAGE.get('invalid phone', AMBUSH)
 
        error_ = ERROR_MESSAGE.get('UnexpectedError', [AMBUSH])[0]
        try:
            result = handler(user_command, contact_dictionary, path_file)

        except KeyError as error:
            return f'{error_}\n{error}\n'

        except ValueError as error:
            return f'{error_}\n{error}\n'

        except IndexError as error:
            return f'{error_}\n{error}\n'
            
        except Exception as error:
            return f'{error_}\n{error}\n'

        if result is None:
            return ERROR_MESSAGE.get('UnpredictableError', [AMBUSH])[0]

        return result

    return exception_function
