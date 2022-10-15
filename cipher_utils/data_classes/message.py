from dataclasses import dataclass


@dataclass
class Message:
    _message: str

    def __init__(self, message: str):
        self._message = message.upper()

    def get_char_at(self, index: int):
        return self._message[index]

    def get_length(self):
        return len(self._message)

    def __repr__(self) -> str:
        return f'{self._message}'
