"""Module used for testing Cube class
"""
from py_utils.math_utils.cube.cube import Cube

def main() -> None:
    """Create an instance of the Cube class and test some of it's functions.
    
        Args: 
            None

        Returns: 
            None
    
        Raises:
            None
    """
    cube_length = 3

    cube = Cube(cube_length)
    cube.print_cube()

if __name__ == '__main__':
    main()
