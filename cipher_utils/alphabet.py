"""Module alphabet.py
"""
from python_utils.cipher_utils.data_classes.constants import Constants
from python_utils.cipher_utils.data_classes.shift_degree import ShiftDegree

import string

class Alphabet:
    """Class Alphabet
    """
    def __init__(self, shift_degree: ShiftDegree) -> None:
        """Generate the alphabet
        
        Args:
            shift_degree: The degree by which we want to shift the alphabet being
                          created.

        Returns:
            None

        Raises:
            None
        """
        self._alphabet = self.generate_alphabet(shift_degree)

    @property
    def alphabet(self) -> list[str]:
        """Get _alphabet"""
        return self._alphabet

    def get_char_at(self, index: int) -> str:
        """Return character at index

        Args:
            index: The index of the character to return

        Returns:
            The character at index
        """
        return self._alphabet[index]

    def set_char_at(self, index: int, new_char: str) -> None:
        """Replace character at index with a new character

        Args:
            index: The index of the character we want to replace

            new_char: The new character which will replace the old one

        Returns:
            None
        """
        self._alphabet[index] = new_char

    def generate_alphabet(self, shift_degree: ShiftDegree) -> list[str]:
        """Generate the alphabet array

        Args:
            shift_degree: The degree by which we want to shift the alphabet

        Returns:
            None
        """
        alphabet = string.ascii_uppercase

        return list(alphabet[shift_degree.shift_degree:] + alphabet[:shift_degree.shift_degree])


    def __repr__(self) -> str:
        """Return a string representation of the alphabet array

        Args:
            None

        Returns:
            String representation of the alphabet array
        """
        alphabet_string = ''

        for index, val in enumerate(self.alphabet):
            if index != (len(self.alphabet) - 1):
                alphabet_string += f'{val},'
            else:
                alphabet_string += f'{val}.'

        return alphabet_string
    
