import numpy as np

class Grid:
    """
    Comment
    """
    def __init__(self, length: int, width: int, initial_element_value: int = 0) -> None:
        self.grid = []
        self.is_initialized: bool
        self.length = length
        self.width = width
        self.initial_element_value = initial_element_value

        self.initialize(length, width)

    """
    Property Getters / Setters
    """
    @property
    def grid(self) -> list[int]:
        return self.__grid

    @grid.setter
    def grid(self, grid: list[int]) -> None:
        self.__grid = grid

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        self.__length = length
    
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        self.__width = width

    @property
    def initial_element_value(self) -> int:
        return self.__initial_element_value

    @initial_element_value.setter
    def initial_element_value(self, initial_element_value: int) -> None:
        self.__initial_element_value = initial_element_value

    @property
    def is_initialized(self) -> bool:
        return self.__is_initialized

    @is_initialized.setter
    def is_initialized(self, is_intialized: bool) -> None:
        self.__is_initialized = is_intialized

    @property
    @staticmethod
    def min_horizontal_boundary() -> int:
        return 0

    @property
    @staticmethod
    def min_vertical_boundary() -> int:
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

    @property
    def value_at_index(self, row_col_position: list[int]) -> int:
        value_at_index = 0

        if self.is_valid_grid_position(row_col_position):
            value_at_index = self.grid[row_col_position[0]][row_col_position[1]]

        return value_at_index

    @grid.setter
    def value_at_index(self, row_col_position: list[int], val: int) -> None:
        if self.is_valid_position(row_col_position):
            self.grid[row_col_position[0]][row_col_position[1]] = val

    """
    Custom Functions
    """
    def is_valid_dimension(self, length: int, width: int) -> bool:
        is_valid_dimension = False

        if length > 0 and width > 0:
            is_valid_dimension = True

        return is_valid_dimension

    def is_valid_position(self, row_col_position: list[int]) -> bool:
        is_valid_position = False

        if (self.min_horizontal_boundary <= row_col_position[0] <= self.max_horizontal_boundary) and \
           (self.min_vertical_boundary <= row_col_position[1] <= self.max_vertical_boundary):
            is_valid_position = True

        return is_valid_position

    def initialize(self, length: int, width: int) -> None:
        self.is_initialized = False

        if self.is_valid_dimension(length, width):
            self.grid = np.full((length, width), self.initial_element_value)

        if self.length > 0:
            self.is_initialized = True

    def reset_values(self) -> None:
        for row in range(self.length):
            for col in range(self.width):
                self.grid[row][col] = self.initial_element_value

    def print_information(self) -> None:
        pass

    def print_coordinates(self) -> None:
        padding = len(str(max(self.max_horizontal_boundary, self.max_vertical_boundary)))

        for row in range(self.length):
            for col in range(self.width):
                print(f'[{row:0{padding}},{col:0{padding}}] ', end='')
            print()
        print()

    def print_values(self) -> None:
        for row in range(self.length):
            print('[', end='')
            for col in range(self.width):
                print(f'{self.value_at_index[row, col]}', end='')

                if col < self.max_vertical_boundary:
                    print(',', end='')
            print(']')
        print()
