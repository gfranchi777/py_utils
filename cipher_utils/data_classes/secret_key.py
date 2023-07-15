from dataclasses import dataclass


@dataclass
class SecretKey:
    _secret_key: str

    def __init__(self, secret_key: str):
        self._secret_key = secret_key.upper().replace(' ','')

    def __repr__(self) -> str:
        return f'{self._secret_key}'
