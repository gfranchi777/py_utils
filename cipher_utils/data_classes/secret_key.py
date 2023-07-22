"""Module secret_key
"""
from dataclasses import dataclass

@dataclass
class SecretKey:
    """Class SecretKey
    """
    @property
    def secret_key(self) -> str:
        """Get _secret_key"""
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key: str) -> None:
        """Set _secret_key"""
        self._secret_key = secret_key

    def __init__(self, secret_key: str):
        self._secret_key: str

        self.secret_key(secret_key.upper().replace(' ',''))

    def __repr__(self) -> str:
        return f'{self.secret_key}'
