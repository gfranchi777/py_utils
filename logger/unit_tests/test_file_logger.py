from utils.logger.file_logger import FileLogger
from utils.logger.logger import Logger


def main() -> None:
    file_logger = FileLogger("test_file_logger", "test_log.txt")
 
    test_protocol(file_logger)

def test_protocol(logger: Logger) -> None:
    logger.debug("test_protocol", "This Is A Debug Message")
    logger.error("test_protocol", "This Is An Error Message")
    logger.info("test_protocol", "This Is An Info Message")

if __name__ == "__main__":
    main()
