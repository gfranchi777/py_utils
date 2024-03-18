from python_utils.cipher_utils.alphabet import Alphabet
from python_utils.cipher_utils.data_classes.constants import Constants
from python_utils.cipher_utils.data_classes.shift_degree import ShiftDegree

def main() -> None:
    for i in range(0,Constants.NUM_LETTERS_IN_ALPHABET):
        shift_degree = ShiftDegree(i)

        alphabet = Alphabet(shift_degree)

        print(repr(alphabet))
    
if __name__ == "__main__":
    main()
