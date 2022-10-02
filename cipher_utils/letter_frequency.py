from os.path import exists

class LetterFrequency:
    #
    # Variables
    #
    letter_frequency = {}

    #
    # Functions`
    #

    def __init__(self,frequencyFilePath: str):
        if exists(frequencyFilePath):
            self.genLetterFrequency(frequencyFilePath)
        else:
            print('[ERROR]: File ' + frequencyFilePath + ' does not exist.')

    def generateLetterFrequency(self, frequencyFilePath: str):
        with open(frequencyFilePath,"r") as frequencyFile:
            for line in frequencyFile:
                (letter,frequency) = line.split(':')
                self.letter_frequency[str(letter)] = str(frequency).replace('\n','')

    def printLetterFrequency(self):
        for key in self.letter_frequency:
            if float(self.letter_frequency[key]) < 10:
                print(key + ': 0' + self.letter_frequency[key])
            else:
                print(key + ': ' + self.letter_frequency[key])
