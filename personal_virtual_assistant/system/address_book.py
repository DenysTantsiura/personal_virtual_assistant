from collections import UserDict
from datetime import datetime, timedelta

from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE,
)


class AddressBook(UserDict):
    """A class of Address book."""

    def __str__(self) -> str:
        abook0 = OTHER_MESSAGE.get('ABook', [AMBUSH])[0]
        return f'{abook0}{self.data})'

    def add_record(self, record) -> None:  # record: Record
        """Adds a new record to the address book dictionary."""
        self.data[record.name.value] = record
    
    def show_happy_birthday(self, meantime: int) -> list:
        """Return the list of the expected birthday party."""
        start_date = datetime.now().date()
        finish_date = start_date + timedelta(days=meantime)  # main_validator catch
        happy_users = []
        for user in self.data:
            if self.data[user].birthday:
                hot_date = self.data[user].birthday.value.date()
                # if the week is the last of the year:
                delta_next_year = 1 if hot_date.month == (finish_date.year-start_date.year) else 0
                try:
                    hot_date = datetime(year=start_date.year + delta_next_year, month=hot_date.month, day=hot_date.day)

                except ValueError:  # 29.02.YY
                    hot_date = datetime(
                        year=start_date.year + delta_next_year,
                        month=hot_date.month,
                        day=hot_date.day-1) + timedelta(days=1)

                if start_date <= hot_date.date() <= finish_date:
                    happy_users.append(
                        f'''{user}{OTHER_MESSAGE.get('Record', [AMBUSH]*3)[2]}{self.data[user].birthday}''')
        # to dict and sort for date? hot_date?
        return happy_users

    def iterator(self, n_count: int) -> list:
        """Return(yield) of n_count records of all AddressBook."""
        current_value = 0
        dictionary_iterator = iter(self.data)

        while current_value < len(self.data):
            volume = []

            for i in range(n_count):

                try:
                    volume.append(self.data[next(dictionary_iterator)])

                except StopIteration:
                    current_value = len(self.data)

            yield volume

            current_value += n_count

    def remove_record(self, name: str) -> None:
        """Remove a record from the address book dictionary."""
        self.data.pop(name)
