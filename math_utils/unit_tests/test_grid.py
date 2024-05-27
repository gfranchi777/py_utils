"""Module used for testing Grid class
"""
from py_utils.math_utils.grid.grid import Grid
from py_utils.math_utils.types.grid_types import GridTypes

def main() -> None:
    """Create an instance of the Grid class and test some of it's functions.

        Args: 
            None

        Returns: 
            None
    
        Raises:
            None
    """
    length = 3
    width = 3

    grid = Grid(length, width, GridTypes.INT)
    grid.print_coordinates()

if __name__ == '__main__':
    main()
