from utils.logger.console_logger import ConsoleLogger
from utils.logger.logger import Logger


def main() -> None:
    console_logger = ConsoleLogger("test_console_logger")

    test_protocol(console_logger)

def test_protocol(logger: Logger) -> None:
    logger.debug("test_protocol", "This Is A Debug Message")
    logger.error("test_protocol", "This Is An Error Message")
    logger.info("test_protocol", "This Is An Info Message")

if __name__ == "__main__":
    main()
