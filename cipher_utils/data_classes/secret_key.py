'''Module secret_key
'''
from dataclasses import dataclass

@dataclass
class SecretKey:
    '''Class SecretKey
    '''
    def __init__(self, secret_key: str):
        self._secret_key = secret_key.upper().replace(' ','')

    @property
    def secret_key(self) -> str:
        '''Get _secret_key'''
        return self._secret_key

    def __repr__(self) -> str:
        return f'{self.secret_key}'

