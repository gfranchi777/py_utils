"""Dataclass used to represent a cleat text or cipher text message.
"""
from dataclasses import dataclass


@dataclass
class Message:
    """Dataclass used to represent a cleat text or cipher text message.
    """

    def __init__(self, message: str):
        self._message = message.upper()

    @property
    def message(self) -> str:
        """Get _message"""
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """Set _message"""
        self._message = message

    def get_char_at(self, char_index: int) -> str:
        """Get character at index char_index"""
        return self._message[char_index]

    def __repr__(self) -> str:
        return f'{self.message}'
