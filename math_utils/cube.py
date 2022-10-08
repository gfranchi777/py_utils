import numpy as np

from math_utils.grid import Grid

class Cube:
    def __init__(self, length: int) -> None:
        self.cube = {
            "F": Grid,
            "B": Grid,
            "U": Grid,
            "D": Grid,
            "L": Grid,
            "R": Grid
        }

        self.cube_faces = {
            "F": 0,
            "B": 1,
            "U": 2,
            "D": 3,
            "L": 4,
            "R": 5
        }

        self.np_cube: np.ndarray[int] 

        self.cube_boundaries: list[int]

        self.initialize_cube(length)

    @property
    def np_cube(self) -> np.ndarray[int]:
        return self.__np_cube
    
    @np_cube.setter
    def np_cube(self, np_cube: np.ndarray[int]) -> None:
        self.__np_cube = np_cube

    @property
    def cube_boundaries(self) -> list[int]:
        return [self.np_cube.shape[0], self.np_cube.shape[1], self.np_cube.shape[2]]

    @cube_boundaries.setter
    def cube_boundaries(self, cube_boundaries: list[int]) -> None:
        self.__cube_boundaries = cube_boundaries

    @staticmethod
    def is_valid_length(length: int) -> bool:
        return length > 1

    def initialize_cube(self, length: int) -> None:
        if self.is_valid_length(length):
            for side in self.cube:
                for row in range(length):
                    self.cube[side] = Grid(length, length)

    def numpy_initialize_cube(self, length: int) -> None:
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
