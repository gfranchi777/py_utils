"""Module shift_degree
"""
from dataclasses import dataclass

@dataclass
class ShiftDegree:
    """Class ShiftDegree
    """

    def __init__(self, shift_degree: int) -> None:
        try:
            self._shift_degree = int(shift_degree)
        except ValueError:
            print(f'Invalid Integer Value Passed To Initializer.')

    @property
    def shift_degree(self) -> int:
        """Get _shift_degree"""
        return self._shift_degree
    
    def __repr__(self) -> str:
        return f'{self.shift_degree}'
