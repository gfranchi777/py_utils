from utils.math_utils.cube import Cube

"""
Script used to test the cube.py modules Cube class
"""
def main() -> None:
    cube_length = 3

    cube = Cube(cube_length)
    cube.print_cube()

if __name__ == '__main__':
    main()
