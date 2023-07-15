import numpy as np
from general.printing import Printing


def main() -> None:
    printing = Printing()

    printing.print_1d_array(np.random.randint(low=0, high=1000, size=5))
    printing.print_2d_array(np.random.randint(low=0, high=1000, size=(5, 5)))
    printing.print_3d_array(np.random.randint(low=0, high=1000000, size=(5, 5, 5)))


if __name__ == "__main__":
    main()
