import numpy as np
from utils.math_utils.grid import Grid


class Cube:
    def __init__(self, length: int) -> None:
        self._cube = {
            "F": Grid,
            "B": Grid,
            "U": Grid,
            "D": Grid,
            "L": Grid,
            "R": Grid
        }

        self._cube_faces = {
            "F": 0,
            "B": 1,
            "U": 2,
            "D": 3,
            "L": 4,
            "R": 5
        }

        self._np_cube: np.ndarray

        self._cube_boundaries: list[int]

        self.initialize_cube(length)

    @property
    def np_cube(self) -> np.ndarray:
        return self._np_cube

    @np_cube.setter
    def np_cube(self, np_cube: np.ndarray) -> None:
        self._np_cube = np_cube

    @property
    def cube_boundaries(self) -> list[int]:
        return [self.np_cube.shape[0], self.np_cube.shape[1], self.np_cube.shape[2]]

    @cube_boundaries.setter
    def cube_boundaries(self, cube_boundaries: list[int]) -> None:
        self._cube_boundaries = cube_boundaries

    @staticmethod
    def is_valid_length(length: int) -> bool:
        return length > 1

    def initialize_cube(self, length: int) -> None:
        self.np_cube = np.zeros((6, length, length), dtype=int)

    def print_cube(self) -> None:
        for i, i_val in enumerate(self.np_cube):
            print(f'Cube Face {i}:\n[')
            for j, j_val in enumerate(i_val):
                print(' [', end='')
                for k, k_val in enumerate(j_val):
                    print(str(self.np_cube[i][j][k_val]), end='')
                    
                    if k < self.cube_boundaries[1] - 1:
                        print(',', end='')
                print(']')
            print(']')
