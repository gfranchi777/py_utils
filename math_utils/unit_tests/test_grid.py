import timeit

from math_utils.grid import Grid

"""
Script used to test the grid.py modules Grid class
"""
def main() -> None:
    length = 3
    width = 3

    grid = Grid(length, width)
    grid.print_information()
    grid.print_coordinates()
    grid.print_values()

if __name__ == '__main__':
    main()