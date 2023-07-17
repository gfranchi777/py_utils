import numpy

from enum import Enum

class GridTypes(Enum):
    """Define the types of grids that are supported.
    Each GridType is a dictionary containing a data_type and initial_value.
    """
    INT = {
        "data_type": numpy.int_,
        "initial_value": 0
    }

    STRING = {
        "data_type": numpy.str_,
        "initial_value": '-'
    }
