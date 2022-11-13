from collections import UserDict

from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE,
)


class AddressBook(UserDict):
    """A class of Address book."""

    def __str__(self) -> str:
        ABOOK0 = OTHER_MESSAGE.get('ABook', [AMBUSH])[0]
        return f'{ABOOK0}{self.data})'

    def add_record(self, record) -> None:  # record: Record
        """Adds a new record to the address book dictionary."""
        self.data[record.name.value] = record

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
