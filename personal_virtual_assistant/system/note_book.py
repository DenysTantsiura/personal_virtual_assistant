from collections import UserDict

from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE,
)


class NoteBook(UserDict):
    """A class of note-book."""

    def __str__(self) -> str:
        nbook0 = OTHER_MESSAGE.get('NBook', [AMBUSH])[0]
        return f'{nbook0}{list(self.data.keys())})'

    def add_record(self, record) -> None:  # record: Record
        """Adds a new record to the note book dictionary."""
        self.data[record.name] = record

    def iterator(self, n_count: int) -> list:
        """Return(yield) of n_count records of all noteBook."""
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
        """Remove a record from the note book dictionary."""
        self.data.pop(name)

    def sort_by_tags(self) -> list:
        """Rreturn list of notenames sorted by tags."""
        tags = []
        for note in self.data.values():
            tags.extend(note.tags)
        tags = list(set(tags))
        tags.sort()

        return list(dict.fromkeys([note.name for tag in tags for note in self.data.values() if tag in note.tags]))
