"""Module grid
"""
import random
import sys
from enum import Enum

import numpy

class GridTypes(Enum):
    """Define the types of grids that are supported.
    Each GridType is a dictionary containing a data_type and initial_value.
    """
    INT = {
        "data_type": numpy.int_,
        "initial_value": 0
    }

    STRING = {
        "data_type": numpy.str_,
        "initial_value": '-'
    }


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
    def __init__(self, length: int, width: int, grid_type: GridTypes) -> None:
        if self.is_valid_dimension(length, width):
            self._is_initialized = False
            self._length = length
            self._width = width
            self._type = grid_type

            self._grid = numpy.empty((length, width), dtype=grid_type.value["data_type"])
        else:
            sys.exit(
                "Invalid Grid Dimensions.\n \
                     Length And Width Must Be Larger Than 0."
            )

    @property
    def grid(self) -> object:
        return self._grid

    @grid.setter
    def grid(self, grid: object) -> None:
        self.grid = grid
   
    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self.length = length

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self.width = width

    @property
    def type(self) -> GridTypes:
        return self._type

    @property
    def is_initialized(self) -> bool:
        return self._is_initialized

    @is_initialized.setter
    def is_initialized(self, is_intialized: bool) -> None:
        self.is_initialized = is_intialized

    @property
    def min_horizontal_boundary(self) -> int:
        return self.length - self.length

    @property
    def min_vertical_boundary(self) -> int:
        return 0

    @property
    def max_horizontal_boundary(self) -> int:
        return self.length - 1

    @property
    def max_vertical_boundary(self) -> int:
        return self.width - 1

    @property
    def min_index(self) -> list[int]:
        return [self.min_horizontal_boundary, self.min_vertical_boundary]

    @property
    def max_index(self) -> list[int]:
        return [self.max_horizontal_boundary, self.max_vertical_boundary]

    def is_valid_dimension(self, length: int, width: int) -> bool:
        is_valid_dimension = False

        if length > 0 and width > 0:
            is_valid_dimension = True

        return is_valid_dimension

    def is_valid_position(self, row_col_position: list[int]) -> bool:
        is_valid_position = False

        if (
            self.min_horizontal_boundary
            <= row_col_position[0]
            <= self.max_horizontal_boundary
        ) and (
            self.min_vertical_boundary
            <= row_col_position[1]
            <= self.max_vertical_boundary
        ):
            is_valid_position = True

        return is_valid_position

    def gen_random_coordinate(self, num_coords: int) -> list[int]:
        random_coords = []

        for _ in range(num_coords):
            random_coords.insert(
                random.randint(
                    self.min_horizontal_boundary, self.max_horizontal_boundary
                ),
                random.randint(
                    self.min_horizontal_boundary, self.max_horizontal_boundary
                ),
            )

        return random_coords

    def initialize(self) -> None:
        for row, row_val in enumerate(self._grid):
            for col, col_val in enumerate(row_val):
                self._grid[row][col] = self.type.value["initial_value"]

    def print_coordinates(self) -> None:
        padding = len(
            str(max(self.max_horizontal_boundary, self.max_vertical_boundary))
        )

        for row, row_val in enumerate(self._grid):
            for col_val in row_val:
                print(f"[{row:0{padding}},{col_val:0{padding}}] ", end="")
            print()
        print()

    def print_values(self, values: list[list[int]], no_new_line: bool = True) -> None:
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
