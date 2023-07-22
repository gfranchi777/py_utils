"""Module printing
"""
import numpy as np

class Printing:
    """Class Printing
    """
    def __init__(self) -> None:
        pass

    def print_1d_array(self, array: np.ndarray) -> None:
        """Print the contents of a normal array
        
        Args:
            array: A standard 1D array

        Returns:
            None
        """
        print(f"{array}\n")

    def print_2d_array(self, array: np.ndarray) -> None:
        """Print the contents of a 2d array
        
        Args:
            array: A 2D array

        Returns:
            None
        """
        print("[")

        for row, row_val in enumerate(array):
            print(f"  {row_val}", end="")

            if row < len(array) - 1:
                print(",")

        print("\n]\n")

    def print_3d_array(self, array: np.ndarray) -> None:
        """Print the contents of a 2d array
        
        Args:
            array: A 3D array

        Returns:
            None
        """
        print("[")

        for width, width_val in enumerate(array):
            print("  [")

            for row, row_val in enumerate(width_val):
                print(f"    {row_val}", end="")

                if row < len(width_val) - 1:
                    print(",")

            print("\n  ]", end="")

            if width < len(array) - 1:
                print(",")

        print("\n]\n")
