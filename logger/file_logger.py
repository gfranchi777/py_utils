from datetime import datetime

import pytz
from utils.logger.logger import LogMessage, MessageType, TimeZone


class FileLogger:

    def __init__(self, calling_class: str) -> None:
        self._log_message = LogMessage(calling_class=calling_class)

    def _log(self, message_type: MessageType, calling_method: str, message: str) -> None:
        print(self._prepare_log(message_type, calling_method, message))

    def _prepare_log(self, message_type: MessageType, calling_method: str, message: str) -> LogMessage:
        self._log_message.timestamp = datetime.now(pytz.timezone(TimeZone.EASTERN_STANDARD.value))
        self._log_message.type = message_type
        self._log_message.calling_method = calling_method
        self._log_message.message = message

        return self._log_message

    def debug(self, calling_method: str, message: str) -> None:
        self._log(MessageType.DEBUG, calling_method, message)

    def error(self,calling_method: str,  message: str) -> None:
        self._log(MessageType.ERROR, calling_method, message)

    def info(self, calling_method: str, message: str) -> None:
        self._log(MessageType.INFO, calling_method, message)
