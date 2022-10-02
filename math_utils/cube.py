import numpy as np

from math_utils.grid import Grid

class Cube:
    #
    # Variables
    #

    cube = {
        "F": Grid,
        "B": Grid,
        "U": Grid,
        "D": Grid,
        "L": Grid,
        "R": Grid
    }

    cube_faces = {
        "F": 0,
        "B": 1,
        "U": 2,
        "D": 3,
        "L": 4,
        "R": 5
    }

    np_cube: np.ndarray[int]

    #
    # Functions
    #

    def __init__(self, length: int) -> None:
        self.initializeCube(length)

    def getLength(self):
        return self.length

    def getCubeBoundaries(self) -> list[int]:
        return [self.np_cube.shape[0], self.np_cube.shape[1], self.np_cube.shape[2]]

    @staticmethod
    def isValidLength(length: int) -> bool:
        return length > 1

    def initializeCube(self, length: int) -> None:
        if self.isValidLength(length):
            for side in self.cube:
                for row in range(length):
                    self.cube[side] = Grid(length, length)

    def numpyInitializeCube(self, length: int) -> None:
        self.np_cube = np.zeros((6, length, length), dtype=int)

    def printCube(self) -> None:
        for side in self.cube:
            print(str(side) + " Side: ")
            self.cube[side].printGridValues()
    
    def printNumpyCube(self) -> None:
        cube_boundaries = self.getCubeBoundaries()

        for i in range(cube_boundaries[0]):
            print('[')
            for j in range(cube_boundaries[1]):
                print('[', end='')
                for k in range(cube_boundaries[2]):
                    print(str(self.np_cube[i][j][k]), end='')

                    if k < cube_boundaries[1] - 1:
                        print(',', end='')
                print(']')
            print(']')
