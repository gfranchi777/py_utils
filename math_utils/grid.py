import numpy as np

class Grid:
    #
    # Variables
    #
    length: int
    width: int

    initial_element_value = 0

    grid = []
    is_initialized: bool

    #
    # Functions
    #
    def __init__(self, length: int, width: int) -> None:
        self.initializeGrid(length, width)

    def getGrid(self) -> list[int]:
        return self.grid

    def getLength(self) -> int:
        return self.length

    def getWidth(self) -> int:
        return self.width

    def getInitialElementValue(self) -> int:
        return self.initial_element_value

    @staticmethod
    def getMinHorizontalBoundary() -> int:
        return 0

    @staticmethod
    def getMinVerticalBoundary() -> int:
        return 0

    def getMaxHorizontalBoundary(self) -> int:
        return self.length - 1

    def getMaxVerticalBoundary(self) -> int:
        return self.width - 1

    def getMinIndex(self):
        return [self.getMinHorizontalBoundary(), self.getMinVerticalBoundary()]
    
    def getMaxIndex(self):
        return [self.getMaxHorizontalBoundary(), self.getMaxVerticalBoundary()]

    def getValueAtIndex(self, row_col_position: list[int]) -> int:
        element_at_index = 0

        if self.isValidGridPosition(row_col_position):
            element_at_index = self.grid[row_col_position[0]][row_col_position[1]]

        return element_at_index

    def setValueAtIndex(self, row_col_position: list[int], val: int) -> None:
        if self.isValidGridPosition(row_col_position):
            self.grid[row_col_position[0]][row_col_position[1]] = val

    def isGridInitialized(self):
        return self.is_initialized

    def isValidGridDimension(self, length: int, width: int) -> None:
        is_valid_grid_dimension = False

        if length > 0 and width > 0:
            is_valid_grid_dimension = True

        return is_valid_grid_dimension

    def isValidGridPosition(self, row_col_position: list[int]) -> bool:
        is_valid_gird_position = False

        if (self.getMinHorizontalBoundary() <= row_col_position[0] <= self.getMaxHorizontalBoundary()) and \
           (self.getMinVerticalBoundary() <= row_col_position[1] <= self.getMaxVerticalBoundary()):
            is_valid_gird_position = True

        return is_valid_gird_position

    def initializeGrid(self, length: int, width: int) -> None:
        self.is_initialized = False

        if self.isValidGridDimension:
            self.length = length
            self.width = width
            self.grid = np.full((length, width), self.initial_element_value)

        if len(self.grid) > 0:
            self.is_initialized = True

    def resetGridValues(self) -> None:
        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                self.grid[row][col] = self.initial_element_value

    def printGridCoordinates(self) -> None:
        for row in range(self.getLength()):
            for col in range(self.getWidth()):
                print('[', end='')

                if row < 10:
                    print('0', end='')

                print(str(row) + ',', end='')

                if col < 10:
                    print('0', end='')

                print(str(col) + '] ', end='')
            print()
        print()

    def printGridValues(self) -> None:
        for row in range(self.getLength()):
            print('[', end='')
            for col in range(self.getWidth()):
                print(self.getValueAtIndex([row, col]), end='')
                if col < self.getMaxHorizontalBoundary():
                    print(',', end='')
            print(']')
        print()
