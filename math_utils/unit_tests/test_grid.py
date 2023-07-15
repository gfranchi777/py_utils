
from python_utils.math_utils.grid.grid import Grid, GridTypes

def main() -> None:
    length = 3
    width = 3

    grid = Grid(length, width, GridTypes.INT)
    grid.print_coordinates()

if __name__ == '__main__':
    main()
