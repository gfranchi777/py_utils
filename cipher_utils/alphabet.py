from . import constants
from shift_degree import ShiftDegree


class Alphabet:
    #
    # Variables
    #
    alphabet = []

    #
    # Functions
    #

    def __init__(self, shift_degree: ShiftDegree):
        self.generateAlphabet(shift_degree)
    
    def getAlphabet(self):
        return self.alphabet

    def getCharAt(self, index):
        return self.alphabet[index]
    
    def getLength(self):
        return len(self.alphabet)

    def setCharAt(self, index: int, new_char: str):
        self.aphabet[index] = new_char

    def generateAlphabet(self, shift_degree: ShiftDegree):
        alphabet = []

        for i in range(constants.NUM_LETTERS_IN_ALPHABET - shift_degree.getShiftDegree()):
            alphabet.append(chr((constants.ASCII_UPPER_CASE_LETTER_START + shift_degree.getShiftDegree()) + i))

        curr_num_letters = len(alphabet)

        for i in range(curr_num_letters, constants.NUM_LETTERS_IN_ALPHABET):
            alphabet.append(chr(constants.ASCII_UPPER_CASE_LETTER_START + shift_degree.getShiftDegree() -
                                constants.NUM_LETTERS_IN_ALPHABET + i))

        self.alphabet = alphabet

    def toString(self):
        alphabet_string = ''
        
        for i in range(len(self.alphabet)):
            alphabet_string = alphabet_string + self.alphabet[i]

        return alphabet_string
    
    def printAlphabet(self):
        for i in range(len(self.alphabet)):
            if i != (len(self.alphabet) - 1):
                print((self.alphabet[i] + ' '), end='')
            else:
                print((self.alphabet[i] + '.'), end='\n')
