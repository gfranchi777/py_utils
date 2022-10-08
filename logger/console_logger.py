from datetime import datetime
from logger.logger import MessageType, LogMessage

class ConsoleLogger:

    _calling_class: str

    def __init__(self, calling_class: str) -> None:
       self._calling_class = calling_class

    def debug(self, calling_method: str, message: str) -> None:
        log_message = LogMessage(timestamp=datetime.now(), type=MessageType.DEBUG, 
                                 calling_class = self._calling_class, calling_method=calling_method,
                                 message=message)

        print(log_message)

        del log_message
    
    def error(self,calling_method: str,  message: str) -> None:
        log_message = LogMessage(timestamp=datetime.now(), type=MessageType.ERROR, 
                                 calling_class = self._calling_class, calling_method=calling_method,
                                 message=message)

        print(log_message)

        del log_message

    def info(self, calling_method: str, message: str) -> None:
        log_message = LogMessage(timestamp=datetime.now(), type=MessageType.INFO, 
                                 calling_class = self._calling_class, calling_method=calling_method,
                                 message=message)

        print(log_message)
    
        del log_message
