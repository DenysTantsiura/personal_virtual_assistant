from datetime import datetime
import re
from typing import Union

from .constant_config import (
    AMBUSH,
    PREFORMATING_PHONE, 
    PREFORMATING_EMAIL1, 
    PREFORMATING_EMAIL2, 
    WARNING_MESSAGE, 
    OTHER_MESSAGE,
)


class Field:  # superclass for all base fields
    """A base class with a simple field."""

    def __init__(self):
        self.__value = None
        self.__bloke = None

    def __str__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value: str):
        self.__value = new_value
    
    @property
    def bloke(self):
        return self.__bloke

    @bloke.setter
    def bloke(self, new_bloke: str):
        self.__bloke = new_bloke


class Name(Field):
    """Class of user name."""
    @Field.value.setter
    def value(self, new_value: str):

        if new_value[0].isalpha():  # not in 'ьъыЫЬЪ\'"[]_0123456789!@$%^&*()-+?<>~`|\\/'
            self._Field__value = new_value

        else:
            print(WARNING_MESSAGE.get('name', AMBUSH))


class Birthday(Field):
    """Class of Birthday data."""
    @Field.value.setter
    def value(self, new_value: str):
        birthday_data = datetime.strptime(new_value, '%Y-%m-%d')

        if birthday_data:
            self._Field__value = birthday_data

        else:
            print(WARNING_MESSAGE.get('birthday', AMBUSH))

    def __str__(self) -> str:
        return f'{self.value.date()}'


class Phone(Field):
    """Class of phone number."""
    @Field.value.setter
    def value(self, new_value: str):

        if re.search(PREFORMATING_PHONE, new_value):
            self._Field__value = self.__preformating(new_value)

        else:
            print(WARNING_MESSAGE.get('phone', AMBUSH))
    
    @Field.bloke.setter
    def bloke(self, new_bloke: str):
        self._Field__bloke = new_bloke

    @staticmethod
    def __preformating(value: str) -> str:
        """Preformating of phone string into the form +dd(ddd)ddddddd."""
        value = value.replace('-', '').replace('(', '').replace(')', '')

        value = '('.join((value[: 3], value[3:]))
        value = ')'.join((value[: 7], value[7:]))
 
        return value


class Details(Field):
    """Details information of user."""
    @Field.value.setter
    def value(self, new_value: str):
        self._Field__value = new_value
    
    @Field.bloke.setter
    def bloke(self, new_bloke: str):
        self._Field__bloke = new_bloke


class Email(Field):
    """Class of user Email."""
    @Field.value.setter
    def value(self, new_value: str):

        if re.search(PREFORMATING_EMAIL1, new_value) or\
             re.search(PREFORMATING_EMAIL2, new_value):
            self._Field__value = self.new_value.strip()

        else:
            print(WARNING_MESSAGE.get('email', AMBUSH))
    
    @Field.bloke.setter
    def bloke(self, new_bloke: str):
        self._Field__bloke = new_bloke


class RelatedInformation(Field):
    """Related information of user."""
    @Field.value.setter
    def value(self, new_value: str):
        self._Field__value = new_value

    @Field.bloke.setter
    def bloke(self, new_bloke: str):
        self._Field__bloke = new_bloke


class Record:
    """Record class of users information."""

    def __init__(self, name: str, *phones: str):
        self.name = Name()
        self.name.value = name
        self.phones = []
        self.birthday = None
        self.emails = []
        self.details = None
        self.related_info = None

        if phones:

            for phone in phones:
                self.add_phone(phone)

    def __str__(self) -> str:
        NAME = OTHER_MESSAGE.get('Record', [AMBUSH])[0]
        PHONES = OTHER_MESSAGE.get('Record', [AMBUSH]*2)[1]
        BIRTHDAY = OTHER_MESSAGE.get('Record', [AMBUSH]*3)[2]
        EMAIL = OTHER_MESSAGE.get('Record', [AMBUSH]*4)[3]
        DETAILS = OTHER_MESSAGE.get('Record', [AMBUSH]*5)[4]
        RELATED = OTHER_MESSAGE.get('Record', [AMBUSH]*6)[5]

        return f'{NAME}{self.name}{PHONES}{self.phones}{BIRTHDAY}'\
            f'{self.birthday}{EMAIL}{self.emails}{DETAILS}{self.details}'\
            f'{RELATED}{self.related_info})'

    def add_birthday(self, birthday: str) -> tuple:
        """Adds a new entry for the user's birthday to the address book."""
        if not self.birthday:

            self.birthday = Birthday()
            self.birthday.value = birthday

            return True,

        else:
            BIRTHDAY0 = OTHER_MESSAGE.get('RBirthday', [AMBUSH])[0]
            BIRTHDAY1 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*2)[1]
            return False, f'{BIRTHDAY0}\"{self.name.value}\"{BIRTHDAY1}'

    def add_phone(self, phone_new: str) -> bool:
        """Adds a new entry for the user's phone to the address book."""
        phone_new1 = Phone()
        phone_new1.value = phone_new

        for phone in self.phones:

            if phone_new1 == phone.value:
                
                PHONE0 = OTHER_MESSAGE.get('RPhone', [AMBUSH])[0]
                print(f'\"{phone_new1}\"{PHONE0}\"{self.name.value}\"')

                return False

        self.phones.append(phone_new1)

        return True

    def change_birthday(self, birthday: str) -> tuple:
        """Modify an existing user's birthday entry in the address book."""
        if not self.birthday:
            
            BIRTHDAY2 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*3)[2]
            BIRTHDAY3 = OTHER_MESSAGE.get('RBirthday', [AMBUSH]*4)[3]
            return False, f'{BIRTHDAY2}\"{self.name.value}\"{BIRTHDAY3}'

        else:

            self.birthday = Birthday()
            self.birthday.value = birthday

            return True,

    def change_phone(self, phone_to_change: str, phone_new: str) -> tuple:
        """Modify an existing user's phone entry in the address book."""
        phone_to_change = Phone._Phone__preformating(phone_to_change)
        phone_new = Phone._Phone__preformating(phone_new)
        verdict = False

        for phone in self.phones:

            if phone.value == phone_new:  # new number already in record
                PHONE0 = OTHER_MESSAGE.get('RPhone', [AMBUSH])[0]
                return False, f'\"{phone_new}\"{PHONE0}\"{self.name.value}\"'

            if phone.value == phone_to_change:  # old number not exist in record
                verdict = True

        if not verdict:
            PHONE2 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*3)[2]
            return verdict, f'\"{phone_to_change}\"{PHONE2}\"{self.name.value}\"'

        for index, phone in enumerate(self.phones):

            if phone.value == phone_to_change:
                phone_new_to = Phone()
                phone_new_to.value = phone_new
                self.phones.remove(phone)
                self.phones.insert(index, phone_new_to)

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

    def remove_phone(self, phone_to_remove: str) -> Union[bool, None]:
        """Deleting a phone entry from a user entry in the address book."""
        phone_to_remove = Phone._Phone__preformating(phone_to_remove)

        for phone in self.phones:

            if phone.value == phone_to_remove:
                self.phones.remove(phone)

                return True

        PHONE2 = OTHER_MESSAGE.get('RPhone', [AMBUSH]*3)[2]      
        print(f'\"{phone_to_remove}\"{PHONE2}\"{self.name.value}\"')

    def years_old(self) -> int:
        """Calculate the number of full years of the user on the next birthday."""
        if self.birthday:
           
            user_day = datetime(year=datetime.now().date().year, \
                month=self.birthday.value.month, day=self.birthday.value.day)

            return datetime.now().year - self.birthday.value.year \
                if (user_day.date() - datetime.now().date()).days > 0 \
                else datetime.now().year + 1 - self.birthday.value.year
