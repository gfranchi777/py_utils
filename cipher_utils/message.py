class Message:
    #
    # Variables
    #
    
    message: str 

    #
    # Functions
    #
    
    def __init__(self, message: str):
        self.message = message.upper()
    
    def getMessage(self):
        return self.message

    def setMessage(self, message: str):
        self.message = message

    def getCharAt(self, index: int):
        return self.message[index]
    
    def getLength(self):
        return len(self.message)

    def printMessage(self):
        print(self.message)
