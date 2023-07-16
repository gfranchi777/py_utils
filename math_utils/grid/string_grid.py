from python_utils.math_utils.grid.grid import Grid, GridTypes


class StringGrid(Grid):
    def __init__(self, length: int, width: int) -> None:
        super().__init__(length, width, GridTypes.STRING)

    def get_value_at(self, row_col_position: list[int]) -> str:
        value_at_index = ''

        if self.is_valid_position(row_col_position):
            value_at_index = self._grid[row_col_position[0]][row_col_position[1]]

        return value_at_index

    def set_value_at(self, row_col_position: list[int], value: str) -> None:
        if self.is_valid_position(row_col_position):
            self._grid[row_col_position[0], row_col_position[1]] = value