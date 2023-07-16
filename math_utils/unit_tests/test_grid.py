"""Module used for testing Grid class
"""
from python_utils.math_utils.grid.grid import Grid, GridTypes

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
