"""Module alphabet.py
"""
from python_utils.cipher_utils.data_classes.constants import Constants
from python_utils.cipher_utils.data_classes.shift_degree import ShiftDegree

class Alphabet:
    """Class Alphabet
    """
    _alphabet: list[str]


    def __init__(self, shift_degree: ShiftDegree):
        """Generate the alphabet
        
        Args:
            shift_degree: The degree by which we want to shift the alphabet being
                          created.

        Returns:
            None

        Raises:
            None
        """
        self.generate_alphabet(shift_degree)

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

    def length(self) -> int:
        """Return the length of _alphabet variable

        Args:
            None

        Returns:
            Length of the _alphabet variable
        """
        return len(self._alphabet)

    def set_char_at(self, index: int, new_char: str) -> None:
        """Replace character at index with a new character

        Args:
            index: The index of the character we want to replace

            new_char: The new character which will replace the old one

        Returns:
            None
        """
        self.alphabet[index] = new_char

    def generate_alphabet(self, shift_degree: ShiftDegree) -> None:
        """Generate the alphabet array

        Args:
            shift_degree: The degree by which we want to shift the alphabet

        Returns:
            None
        """
        alphabet = []

        for i in range(Constants.NUM_LETTERS_IN_ALPHABET - shift_degree._shift_degree):
            alphabet.append(chr((Constants.ASCII_UPPER_CASE_LETTER_START + shift_degree._shift_degree) + i))

        curr_num_letters = len(alphabet)

        for i in range(curr_num_letters, Constants.NUM_LETTERS_IN_ALPHABET):
            alphabet.append(chr(Constants.ASCII_UPPER_CASE_LETTER_START + shift_degree._shift_degree -
                                Constants.NUM_LETTERS_IN_ALPHABET + i))

        self.alphabet = alphabet

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
                alphabet_string += f'{val}.\n'

        return alphabet_string
    
