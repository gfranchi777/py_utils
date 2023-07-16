from datetime import datetime

import pytz
from utils.logger.logger import LogMessage, MessageType, TimeZone


class ConsoleLogger:

    """ Initializer """
    def __init__(self, calling_class: str) -> None:
        self._log_message = LogMessage(calling_class)

    """Function which will output the log entry"""
    def _log(self, log_message: LogMessage) -> None:
        print(log_message)

    """ Function which will build a LogMessage """
    def _prepare_log(self, message_type: MessageType, calling_method: str, message: str) -> LogMessage:
        self._log_message.timestamp = datetime.now(pytz.timezone(TimeZone.EASTERN_STANDARD.value))
        self._log_message.type = message_type
        self._log_message.calling_method = calling_method
        self._log_message.message = message

        return self._log_message
    
    """ Function to be called when we want to log a DEBUG message """
    def debug(self, calling_method: str, message: str) -> None:
        self._log(self._prepare_log(MessageType.DEBUG, calling_method, message))

    """ Function to be called when we want to log an ERROR message """
    def error(self, calling_method: str, message: str) -> None:
        self._log(self._prepare_log(MessageType.ERROR, calling_method, message))

    """ Function to be called when we want to log an INFO message """
    def info(self, calling_method: str, message: str) -> None:
        self._log(self._prepare_log(MessageType.INFO, calling_method, message))
