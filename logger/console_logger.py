"""Module console_logger
"""
from datetime import datetime

import pytz
from pyutils.logger.logger import LogMessage, MessageType, TimeZone


class ConsoleLogger:
    """Class ConsoleLogger
    """
    @property
    def log_message(self) -> LogMessage:
         """Get _log_message"""
         return self._log_message
    
    @log_message.setter
    def log_message(self, log_message: LogMessage) -> None:
         """Set _log_message"""
         self._log_message = log_message

    def __init__(self, calling_class: str) -> None:
        self._log_message: LogMessage

        self.log_message(LogMessage(calling_class))

    def _log(self, log_message: LogMessage) -> None:
        """Output the log entry"""
        print(log_message)

    def _prepare_log(self, message_type: MessageType, 
                     calling_method: str, message: str) -> LogMessage:
        """Build a LogMessage"""
        self.log_message.timestamp = datetime.now(pytz.timezone(TimeZone.EASTERN_STANDARD.value))
        self.log_message.type = message_type
        self.log_message.calling_method = calling_method
        self.log_message.message = message

        return self.log_message

    def debug(self, calling_method: str, message: str) -> None:
        """Log a DEBUG message """
        self._log(self._prepare_log(MessageType.DEBUG, calling_method, message))

    def error(self, calling_method: str, message: str) -> None:
        """Log an ERROR message """
        self._log(self._prepare_log(MessageType.ERROR, calling_method, message))

    def info(self, calling_method: str, message: str) -> None:
        """Log an INFO message """
        self._log(self._prepare_log(MessageType.INFO, calling_method, message))
