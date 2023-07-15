"""Module IntGrid
"""
from grid import Grid, GridTypes

class IntGrid(Grid):
    """Create a Grid object with integer values.
    
        Args:
            length:
                The number of rows in the grid.
            width:
                The number of colums in the grid.
        
        Returns:
            None
        
        Raises:
            None
    """
    def __init__(self, length: int, width: int) -> None:
        super().__init__(length, width, GridTypes.INT)
