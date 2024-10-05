"""
Module: grid_types

This module defines the types of grids that are supported.
Each GridType is a dictionary containing a data_type and initial_value.
"""

from enum import Enum

import numpy


class GridTypes(Enum):
    """Define the types of grids that are supported.
    Each GridType is a dictionary containing a data_type and initial_value.
    """

    INT = {"data_type": int, "initial_value": 0}

    STRING = {"data_type": str, "initial_value": "-"}
