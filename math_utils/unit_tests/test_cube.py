from math_utils.cube import Cube


def main() -> None:
    cube_length = 3

    cube = Cube(cube_length)
    cube.printCube()

    cube.numpyInitializeCube(cube_length)
    cube.printNumpyCube()

if __name__ == '__main__':
    main()