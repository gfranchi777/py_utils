from pyutils.cipher_utils.alphabet import Alphabet
from pyutils.cipher_utils.data_classes.constants import Constants

def main() -> None:
    for i in range(0,Constants.NUM_LETTERS_IN_ALPHABET):
        alphabet = Alphabet(i)

        print(repr(alphabet))
    
if __name__ == "__main__":
    main()
