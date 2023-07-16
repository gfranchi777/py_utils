from constants import Constants
from data_classes.shift_degree import ShiftDegree


class Alphabet:
    #
    # Variables
    #
    _alphabet: list[str]

    #
    # Functions
    #

    def __init__(self, shift_degree: ShiftDegree):
        self.generate_alphabet(shift_degree)

    @property
    def alphabet(self) -> list[str]:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, alphabet: list[str]) -> None:
        self._alphabet = alphabet

    def get_char_at(self, index):
        return self.alphabet[index]

    def length(self):
        return len(self.alphabet)

    def set_char_at(self, index: int, new_char: str):
        self.alphabet[index] = new_char

    def generate_alphabet(self, shift_degree: ShiftDegree):
        alphabet = []

        for i in range(Constants.NUM_LETTERS_IN_ALPHABET - shift_degree._shift_degree):
            alphabet.append(chr((Constants.ASCII_UPPER_CASE_LETTER_START + shift_degree._shift_degree) + i))

        curr_num_letters = len(alphabet)

        for i in range(curr_num_letters, Constants.NUM_LETTERS_IN_ALPHABET):
            alphabet.append(chr(Constants.ASCII_UPPER_CASE_LETTER_START + shift_degree._shift_degree -
                                Constants.NUM_LETTERS_IN_ALPHABET + i))

        self.alphabet = alphabet

    def __repr__(self) -> str:
        alphabet_string = ''

        for index, val in enumerate(self.alphabet):
            if index != (len(self.alphabet) - 1):
                alphabet_string += f'{val},'
            else:
                alphabet_string += f'{val}.\n'

        return alphabet_string
    