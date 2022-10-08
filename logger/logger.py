from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Protocol

class MessageType(Enum):
    DEBUG = '[DEBUG]'
    ERROR = '[ERROR]'
    INFO = '[INFO]'

@dataclass
class LogMessage:
    timestamp: datetime
    type: MessageType
    calling_class: str
    calling_method: str
    message: str

    def __repr__(self) -> str:
        return f'{self.timestamp.strftime("%Y/%m/%d %H:%M:%S")} ' \
               f'{self.type.value} {self.calling_class}.{self.calling_method}() - {self.message}'

class Logger(Protocol):
    def info(self, calling_method: str, message: str) -> None:
        ...
    
    def debug(self, calling_method: str, message: str)-> None:
        ...

    def error(self, calling_method: str, message: str) -> None:
        ...