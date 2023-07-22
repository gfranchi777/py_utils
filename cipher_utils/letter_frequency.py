"""Mofule letter_frequency
"""
from os.path import exists

class LetterFrequency:
    """Class LetterFrequency
    """

    @property
    def letter_frequency(self) -> dict[str]:
        """Get _letter_frequency"""
        return self._letter_frequency

    def __init__(self, frequency_file_path: str) -> None:
        self._letter_frequency = {}

        if exists(frequency_file_path):
            self.genLetterFrequency(frequency_file_path)
        else:
            print('[ERROR]: File ' + frequency_file_path + ' does not exist.')

    def generate_letter_frequency(self, frequency_file_path: str) -> None:
        """Populate the _letter_frequency dictionary with the contents of 
        the frequencey_file.
        
        Args:
            frequency_file_path: The path to the frequency file to parse

        Returns:
            None
        """
        with open(frequency_file_path, mode="r", encoding="None") as frequency_file:
            for line in frequency_file:
                (letter, frequency) = line.split(':')
                self._letter_frequency[str(letter)] = str(frequency).replace('\n','')

    def print_letter_frequency(self) -> None:
        """Print out the contents of the _letter_frequency dictionary

        Args:
            None

        Returns:
            None
        """
        for letter, frequency in self.letter_frequency.items():
            if float(letter) < 10:
                print(letter + ': 0' + frequency)
            else:
                print(letter + ': ' + frequency)
