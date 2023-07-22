"""Module shift_degree
"""
from dataclasses import dataclass

@dataclass
class ShiftDegree:
    """Class ShiftDegree
    """

    @property
    def shift_degree(self) -> int:
        """Get _shift_degree"""
        return self._shift_degree
    
    @shift_degree.setter
    def shift_degree(self, shift_degree: int) -> None:
        """Set _shift_degree"""
        self._shift_degree = shift_degree

    def __init__(self, shift_degree: int) -> None:
        self._shift_degree: int

        self.shift_degree(shift_degree)

    def __repr__(self) -> str:
        return f'{self.shift_degree}'
