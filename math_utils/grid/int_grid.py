from python_utils.math_utils.grid.grid import Grid, GridTypes


class IntGrid(Grid):
    def __init__(self, length: int, width: int) -> None:
        super().__init__(length, width, GridTypes.INT)

    def get_value_at(self, row_col_position: list[int]) -> int:
        value_at_index = 0

        if self.is_valid_position(row_col_position):
            value_at_index = self._grid[row_col_position[0]][row_col_position[1]]

        return value_at_index

    def set_value_at(self, row_col_position: list[int], value: int) -> None:
        if self.is_valid_position(row_col_position):
            self._grid[row_col_position[0], row_col_position[1]] = value