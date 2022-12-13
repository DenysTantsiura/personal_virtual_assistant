import re


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'

TRANSLATION = ('a', 'b', 'v', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h',
               'ts', 'ch', 'sh', 'sch', '', 'y', '', 'e', 'yu', 'ja', 'je',
               'i', 'ji', 'gh')

NORMALIZATION_SCHEME = {}
# creation map(dictionary) for character replacement
for c_symbol, l_symbol in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    NORMALIZATION_SCHEME[ord(c_symbol)] = l_symbol
    NORMALIZATION_SCHEME[ord(c_symbol.upper())] = l_symbol.upper()


def normalize(name: str) -> str:
    """
    Replaces Cyrillic characters with Latin characters in a string.
    Returns the new string.

        Parameters:
            name(str): A simple string.

        Returns:
            new_name(str): Output string.
    """
    new_name = name.translate(NORMALIZATION_SCHEME)
    new_name = re.sub(r'\W', '_', new_name)

    return new_name
