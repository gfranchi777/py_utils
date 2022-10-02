class ShiftDegree:
    #
    # Variables
    #
    
    shift_degree: int

    #
    # Functions
    #

    def __init__(self, shift_degree: int):
        self.shift_degree = shift_degree

    def setShiftDegree(self,shift_degree: int):
        self.shift_degree = shift_degree

    def getShiftDegree(self):
        return self.shift_degree

    def toString(self):
        return str(self.shift_degree)
