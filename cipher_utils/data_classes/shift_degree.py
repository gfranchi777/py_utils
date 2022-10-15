from dataclasses import dataclass


@dataclass
class ShiftDegree:
    _shift_degree: int

    def __repr__(self) -> str:
        return f'{self._shift_degree}'
