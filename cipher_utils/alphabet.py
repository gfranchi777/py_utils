"""Module alphabet.py
"""
from python_utils.cipher_utils.data_classes.constants import Constants

import string

class Alphabet:
    """Class Alphabet
    """
    def __init__(self, offset: int = 0) -> None:
        self._alphabet = self.generate_alphabet(offset)

    @property
    def alphabet(self) -> list[str]:
        return self._alphabet

    def get_char_at(self, index: int) -> str:
        return self._alphabet[index]

    def set_char_at(self, index: int, new_char: str) -> None:
        self._alphabet[index] = new_char

    def generate_alphabet(self, offset: int) -> list[str]:
        alphabet = string.ascii_uppercase

        return list(alphabet[offset:] + alphabet[:offset])


    def __repr__(self) -> str:
        alphabet_string = ''

        for index, val in enumerate(self.alphabet):
            if index != (len(self.alphabet) - 1):
                alphabet_string += f'{val},'
            else:
                alphabet_string += f'{val}.'

        return alphabet_string
    
