from .grid import Grid, GridTypes


class IntGrid(Grid):
    def __init__(self, length: int, width: int) -> None:
        super().__init__(length, width, GridTypes.INT)
