from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Protocol


class MessageType(Enum):
    DEBUG = "[DEBUG]"
    ERROR = "[ERROR]"
    INFO = "[INFO]"

class TimeZone(Enum):
    CENTRAL_STANDARD = "America/Winnipeg",
    EASTERN_STANDARD = "America/Montreal"

@dataclass
class LogMessage:
    timestamp: datetime = field(init=False)
    type: MessageType = field(init=False)
    calling_class: str
    calling_method: str = field(init=False)
    message: str = field(init=False)

    def __repr__(self) -> str:
        return (f'{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")} '
                f'{self.type.value} {self.calling_class}.{self.calling_method}() - {self.message}')

class Logger(Protocol):
    @property
    def _log_message(self) -> LogMessage:
        ...

    '''Function which will output the log entry'''
    def _log(self, log_message: LogMessage) -> None:
        ...

    ''' Function which will build a LogMessage '''
    def _prepare_log(self, message_type: MessageType, calling_method: str, message: str) -> LogMessage:
        ...

    ''' Function to be called when we want to log a DEBUG message '''
    def debug(self, calling_method: str, message: str) -> None:
        ...

    ''' Function to be called when we want to log an ERROR message '''
    def error(self, calling_method: str, message: str) -> None:
        ...

    ''' Function to be called when we want to log an INFO message '''
    def info(self, calling_method: str, message: str) -> None:
        ...
