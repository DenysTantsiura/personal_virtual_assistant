from datetime import datetime
import re
from typing import Union

from .constant_config import (
    AMBUSH,
    BIRTHDAY_FORMAT,
    PREFORMATING_PHONE, 
    PREFORMATING_EMAIL1, 
    PREFORMATING_EMAIL2, 
    WARNING_MESSAGE, 
    OTHER_MESSAGE,
)


class Field:  # superclass for all base fields
    """A base class with a simple field."""

    def __init__(self):
        self._value = None

    def __str__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value: str):
        self._value = new_value
   

class Name(Field):
    """Class of user name."""
    def __init__(self):
        super().__init__()
        self._nickname = None

    @property
    def nickname(self):
        return self._nickname

    @Field.value.setter
    def value(self, new_value: str):

        if new_value[0].isalpha():  # not in 'ьъыЫЬЪ\'"[]_0123456789!@$%^&*()-+?<>~`|\\/'
            self._value = new_value

        else:
            print(WARNING_MESSAGE.get('name', AMBUSH))
    
    @nickname.setter
    def nickname(self, new_nickname: str):

        if new_nickname[0].isalpha():  # not in 'ьъыЫЬЪ\'"[]_0123456789!@$%^&*()-+?<>~`|\\/'
            self._nickname = new_nickname

        else:
            print(WARNING_MESSAGE.get('name', AMBUSH))


class Birthday(Field):
    """Class of Birthday data."""
    @Field.value.setter
    def value(self, new_value: str):
        birthday_data = datetime.strptime(new_value, BIRTHDAY_FORMAT)

        if birthday_data:
            self._value = birthday_data

        else:
            print(WARNING_MESSAGE.get('birthday', AMBUSH))

    def __str__(self) -> str:
        return f'{self.value.date()}'


class Phone(Field):
    """Class of phone number."""
    @Field.value.setter
    def value(self, new_value: str):

        if re.search(PREFORMATING_PHONE, new_value):
            self._value = self._preformating(new_value)

        else:
            print(WARNING_MESSAGE.get('phone', AMBUSH))
    

    @staticmethod
    def _preformating(value: str) -> str:
        """Preformating of phone string into the form +dd(ddd)ddddddd."""
        value = value.replace('-', '').replace('(', '').replace(')', '')

        value = '('.join((value[: 3], value[3:]))
        value = ')'.join((value[: 7], value[7:]))
 
        return value


class Details(Field):
    """Details information of user."""
    # @Field.value.setter
    # def value(self, new_value: str):
    #     self._value = new_value

    pass


class Email(Field):
    """Class of user Email."""
    @Field.value.setter
    def value(self, new_value: str):

        if re.search(PREFORMATING_EMAIL1, new_value) or\
             re.search(PREFORMATING_EMAIL2, new_value):
            self._value = new_value.strip()

        else:
            print(WARNING_MESSAGE.get('email', AMBUSH))
    

class Record:
    """Record class of users information."""

    def __init__(self, name: str, *phones: str):
        self.name = Name()
        self.name.value = name
        self.phones = []
        self.birthday = None
        self.emails = []
        self.details = None  # class()

        if phones:

            for phone in phones:
                self.add_phone(phone)

    def __str__(self) -> str:
        name_ = OTHER_MESSAGE.get('Record', [AMBUSH])[0]
        phones_ = OTHER_MESSAGE.get('Record', [AMBUSH]*2)[1]
        birthday_ = OTHER_MESSAGE.get('Record', [AMBUSH]*3)[2]
        email_ = OTHER_MESSAGE.get('Record', [AMBUSH]*4)[3]
        details_ = OTHER_MESSAGE.get('Record', [AMBUSH]*5)[4]
        # related_ = OTHER_MESSAGE.get('Record', [AMBUSH]*6)[5]

        return f'{name_}{self.name}{phones_}{self.phones}{birthday_}'\
            f'{self.birthday}{email_}{self.emails}{details_}{self.details}'\
            f')'# f'{related_}{self.related_info})'

    def add_birthday(self, birthday: str) -> tuple:
        """Adds a new entry for the user's birthday to the address book."""
        if not self.birthday:

            self.birthday = Birthday()
            self.birthday.value = birthday

            return True,

        else:
            birthday0 = OTHER_MESSAGE.get('RBirthday', [AMBUSH])[0]
            birthday1 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*2)[1]
            return False, f'{birthday0}\"{self.name.value}\"{birthday1}'

    def add_nickname(self, nickname: str) -> tuple:
        """Adds a new entry for the user's name - nickname."""
        if nickname:
            self.name.nickname = nickname
            return True,

        else:
            nickname0 = OTHER_MESSAGE.get('Rnickname', [AMBUSH])[0]
            return False, f'{nickname0}\"{nickname}\"'

    def add_phone(self, phone_new: str) -> bool:
        """Adds a new entry for the user's phone to the address book."""
        phone_new1 = Phone()
        phone_new1.value = phone_new

        for phone in self.phones:

            if phone_new1 == phone.value:
                
                phone0 = OTHER_MESSAGE.get('RPhone', [AMBUSH])[0]
                print(f'\"{phone_new1}\"{phone0}\"{self.name.value}\"')

                return False

        self.phones.append(phone_new1)

        return True
    
    def add_email(self, email_new: str) -> bool:
        """Adds a new entry for the user's email to the address book."""
        email_new1 = Email()
        email_new1.value = email_new

        for email in self.emails:

            if email_new1 == email.value:
                
                email0 = OTHER_MESSAGE.get('REmail', [AMBUSH])[0]
                print(f'\"{email_new1}\"{email0}\"{self.name.value}\"')

                return False

        self.emails.append(email_new1)

        return True

    def change_birthday(self, birthday: str) -> tuple:
        """Modify an existing user's birthday entry in the address book."""
        if not self.birthday:
            
            birthday2 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*3)[2]
            birthday3 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*4)[3]
            return False, f'{birthday2}\"{self.name.value}\"{birthday3}'

        else:

            self.birthday = Birthday()
            self.birthday.value = birthday

            return True,
    
    def change_nickname(self, new_nickname: str) -> tuple:
        """Modify an existing user's nickname entry in the address book."""
        if new_nickname:
            self.name.nickname = new_nickname
            return True,

        else:
            nickname0 = OTHER_MESSAGE.get('Rnickname', [AMBUSH])[0]
            return False, f'{nickname0}\"{new_nickname}\"'


    def change_phone(self, phone_to_change: str, phone_new: str) -> tuple:
        """Modify an existing user's phone entry in the address book."""
        phone_to_change = Phone._preformating(phone_to_change)
        phone_new = Phone._preformating(phone_new)
        verdict = False

        for phone in self.phones:

            if phone.value == phone_new:  # new number already in record
                phone0 = OTHER_MESSAGE.get('RPhone', [AMBUSH])[0]
                return False, f'\"{phone_new}\"{phone0}\"{self.name.value}\"'

            if phone.value == phone_to_change:  # old number not exist in record
                verdict = True

        if not verdict:
            phone2 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*3)[2]
            return verdict, f'\"{phone_to_change}\"{phone2}\"{self.name.value}\"'

        for index, phone in enumerate(self.phones):

            if phone.value == phone_to_change:
                phone_new_to = Phone()
                phone_new_to.value = phone_new
                self.phones.remove(phone)
                self.phones.insert(index, phone_new_to)

                return True,

    def change_email(self, email_to_change: str, email_new: str) -> tuple:
        """Modify an existing user's email entry in the address book."""
        verdict = False

        for email in self.emails:

            if email.value == email_new:  # new email already in record
                email0 = OTHER_MESSAGE.get('REmail', [AMBUSH])[0]
                return False, f'\"{email_new}\"{email0}\"{self.name.value}\"'

            if email.value == email_to_change:  # old email not exist in record
                verdict = True

        if not verdict:
            email2 = OTHER_MESSAGE.get('REmail', [AMBUSH]*3)[2]
            return verdict, f'\"{email_to_change}\"{email2}\"{self.name.value}\"'

        for index, email in enumerate(self.emails):

            if email.value == email_to_change:
                email_new_to = Email()
                email_new_to.value = email_new
                self.emails.remove(email)
                self.emails.insert(index, email_new_to)

                return True,

    def days_to_birthday(self) -> int:
        """Count the number of days until the next birthday of the user."""
        if self.birthday:

            user_day = datetime(year=datetime.now().date().year, \
                month=self.birthday.value.month, day=self.birthday.value.day)

            days_left = user_day.date() - datetime.now().date()

            if days_left.days <= 0:

                user_day = datetime(year=datetime.now().date().year + 1, \
                    month=self.birthday.value.month, day=self.birthday.value.day)

                return (user_day.date() - datetime.now().date()).days

            return days_left.days

    def remove_birthday(self) -> Union[bool, None]:
        """Deleting a birthday entry from a user entry in the address book."""
        if self.birthday:
            self.birthday = None
            return True
    
    def remove_nickname(self) -> Union[bool, None]:
        """Deleting a nickname entry from a user entry in the address book."""
        if self.name.nickname:
            self.name.nickname = None
            return True

    def remove_phone(self, phone_to_remove: str) -> Union[bool, None]:
        """Deleting a phone entry from a user entry in the address book."""
        phone_to_remove = Phone._preformating(phone_to_remove)

        for phone in self.phones:

            if phone.value == phone_to_remove:
                self.phones.remove(phone)

                return True

        phone2 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*3)[2]
        print(f'\"{phone_to_remove}\"{phone2}\"{self.name.value}\"')

    def remove_email(self, email_to_remove: str) -> Union[bool, None]:
        """Deleting a email entry from a user entry in the address book."""
        for email in self.emails:

            if email.value == email_to_remove:
                self.emails.remove(email)

                return True

        email2 = OTHER_MESSAGE.get('REmail', [AMBUSH]*3)[2]
        print(f'\"{email_to_remove}\"{email2}\"{self.name.value}\"')

    def years_old(self) -> int:
        """Calculate the number of full years of the user on the next birthday."""
        if self.birthday:
           
            user_day = datetime(year=datetime.now().date().year, \
                month=self.birthday.value.month, day=self.birthday.value.day)

            return datetime.now().year - self.birthday.value.year \
                if (user_day.date() - datetime.now().date()).days > 0 \
                else datetime.now().year + 1 - self.birthday.value.year
