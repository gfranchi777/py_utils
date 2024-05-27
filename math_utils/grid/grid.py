"""Module grid
"""
import random
import sys

import numpy

from py_utils.math_utils.types.grid_types import GridTypes

class Grid:
    """Create a grid of size length x width and of type GridType
    
        Args:
            length:
                The number of rows in the grid.
            width:
                The number of colums in the grid.
            grid_type:
                The type of grid we will create (GridTypes datatype).
        
        Returns:
            None

        Raises:
            None
    """
    def __init__(self, width: int, length: int, grid_type: GridTypes) -> None:
        if self.is_valid_dimension(length, width):
            self._is_initialized = False
            self._length = length
            self._width = width
            self._type = grid_type

            self._grid = numpy.full((width, length), grid_type.value["initial_value"],
                                    dtype=grid_type.value["data_type"])
        else:
            sys.exit(
                "Invalid Grid Dimensions.\n \
                     Length And Width Must Be Larger Than 0."
            )

    @property
    def grid(self) -> object:
        """Get _grid"""
        return self._grid

    @grid.setter
    def grid(self, grid: object) -> None:
        """Set _grid"""
        self._grid = grid

    @property
    def length(self) -> int:
        """Get _length"""
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        """Set _length"""
        self._length = length

    @property
    def width(self) -> int:
        """Get _width"""
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        """Set _width"""
        self._width = width

    @property
    def type(self) -> GridTypes:
        """Get _type"""
        return self._type

    @property
    def is_initialized(self) -> bool:
        """Get _is_initialized"""
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, is_intialized: bool) -> None:
        """Set _is_initialized"""
        self.is_initialized = is_intialized

    @property
    def min_horizontal_boundary(self) -> int:
        """Get min horizontal bounary"""
        return 0

    @property
    def min_vertical_boundary(self) -> int:
        """Get minimum vertical boundary"""
        return 0

    @property
    def max_horizontal_boundary(self) -> int:
        """Calculate max horizontal boundary"""
        return self.length - 1

    @property
    def max_vertical_boundary(self) -> int:
        """Calculate max vertical boundary"""
        return self.width - 1

    @property
    def min_index(self) -> list[int]:
        """Get minimum grid index"""
        return [self.min_horizontal_boundary, self.min_vertical_boundary]

    @property
    def max_index(self) -> list[int]:
        """Get maximum grid index"""
        return [self.max_horizontal_boundary, self.max_vertical_boundary]

    def is_valid_dimension(self, width: int, length: int) -> bool:
        """Determine if the dimensions being used to create the grid are valid
        
        Args:
            length: 
                length of the grid

            width:
                width of the grid
        
        Returns:

            True if the dimensions passed are valid
            False otherwise
        """
        return (length > 0 and width > 0)

    def is_valid_position(self, row_col_position: list[int]) -> bool:
        """Determine if the position being passed is within the grid bounds
        
        Args:
            row_col_position:
                An array containing an x, y coordinate
        
        Returns:

            True if the coordinates are in the boundaries of the grid
            False otherwise
        """
        is_valid_position = False

        if (
            self.min_vertical_boundary
            <= row_col_position[0]
            <= self.max_vertical_boundary
        ) and (
            self.min_horizontal_boundary
            <= row_col_position[1]
            <= self.max_horizontal_boundary
        ):
            is_valid_position = True

        return is_valid_position

    def gen_random_coordinate(self, num_coords: int) -> list[int]:
        """Generate random coordinates which fall inside the grid boundaries
        
        Args:
            num_coords:
                The number of coordinate pairs to generate

        Returns:

            An array containing num_coords pairs of x, y coordinates within the grid boundaries.
        """
        random_coords = []

        for _ in range(num_coords):
            random_coords.insert(
                random.randint(
                    self.min_vertical_boundary, self.max_vertical_boundary
                ),
                random.randint(
                    self.min_horizontal_boundary, self.max_horizontal_boundary
                ),
            )

        return random_coords

    def initialize(self) -> None:
        """Initialize the grid by filling it with the initial value specified in the GridTypes
        
        Args:
            None
        
        Returns:
            None
        """
        for row, row_val in enumerate(self._grid):
            for col, col_val in enumerate(row_val):
                self._grid[row][col] = self.type.value["initial_value"]

    def print_coordinates(self) -> None:
        """Print out the x,y coordinate pairs in the grid
        
        Args:
            None
        
        Returns:
            None
        """
        padding = len(
            str(max(self.max_vertical_boundary, self.max_horizontal_boundary))
        )

        for row, row_val in enumerate(self._grid):
            for col, col_val in enumerate(row_val):
                print(f"[{row:0{padding}},{col:0{padding}}] ", end="")
            print()
        print()

    def print_values(self, values: list[list[int]], no_new_line: bool = True) -> None:
        """Format and print values in the grid using recursion.

        Args:
            values:
                The list of a list of int which will will print out
            
            no_new_line:
                Specify if on a given recursion we want to print a new line or not
        
        Returns:
            None
        """
        if len(values) > 0:
            print(f"{values[0]}", end="")

            if len(values) > 1:
                if no_new_line:
                    print(" ", end="")
                else:
                    print()
            else:
                print("\n")

            self.print_values(values[1:], no_new_line)
