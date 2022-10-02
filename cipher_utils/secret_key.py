class SecretKey:
    #
    # Variables
    #
    
    secret_key: str

    #
    # Functions
    #

    def __init__(self, secret_key: str):
        self.setSecretKey(secret_key.upper().replace(' ',''))

    def getSecretKey(self):
        return self.secret_key

    def setSecretKey(self, secret_key: str):
        self.secret_key = secret_key
