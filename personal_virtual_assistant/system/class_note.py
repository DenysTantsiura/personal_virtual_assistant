from .constant_config import (
    AMBUSH,
    OTHER_MESSAGE, 
)


class Note:
    """Record class of Note."""

    def __init__(self, name: str, text: str) -> None:
        self.name = name
        self.tags = []
        self.text = text
        for word in text.split(' '):
            if word.startswith('#'):
                self.tags.append(word)

    def __str__(self) -> str:
        name_ = OTHER_MESSAGE.get('Note', [AMBUSH])[0]
        tags_ = OTHER_MESSAGE.get('Note', [AMBUSH]*2)[1]
        text_ = OTHER_MESSAGE.get('Note', [AMBUSH]*3)[2]

        return f'{name_}{self.name}\n{tags_}{self.tags}\n{text_}'\
            f'{self.text}\n'

    def add_tags(self, new_tags: str) -> tuple:
        """Adds a new tag(s) to the note."""
        if new_tags:
            wrong_tags = []
            correct_tags = []
            for word in new_tags.split(' '):
                if word.startswith('#'):
                    self.tags.append(word)
                    correct_tags.append(word) 
                else:
                    wrong_tags.append(word)
            tags0 = OTHER_MESSAGE.get('Rtags', [AMBUSH])[0]
            tags1 = OTHER_MESSAGE.get('Rtags', [AMBUSH] * 2)[1]
            if wrong_tags:
                return False, f'{tags0}: {correct_tags}\n{tags1}{wrong_tags}'
            return True, (correct_tags, wrong_tags)

        return False, f''
    
    def change_note(self) -> tuple:
        """Show for change note, and apply the changes."""
        print(self)  # self.__str__()
        self.name = self.input_with_default(OTHER_MESSAGE.get('Nchange', [AMBUSH])[0], self.name)

        old_tags = self.tags[:]
        self.tags = []
        for tag in self.input_with_default(OTHER_MESSAGE.get('Nchange', [AMBUSH]*2)[1], ' '.join(old_tags)).split(' '):
            if tag.startswith('#'):
                self.tags.append(tag)

        self.text = self.input_with_default(OTHER_MESSAGE.get('Nchange', [AMBUSH]*3)[2], self.text)
        
        return True,

    @staticmethod
    def input_with_default(prompt: str, default: str) -> str:
        bck = chr(8) * len(default)
        result = input(f'{prompt}{default}' + bck)
        return result or default
