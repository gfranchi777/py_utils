from logger.console_logger import ConsoleLogger

def main() -> None:
    logger =  ConsoleLogger("test_console_logger")

    logger.debug("main", "This Is A Debug Message")
    logger.info("main", "This Is An Info Message")
    logger.error("main", "This Is An Error Message")
    
if __name__ == "__main__":
    main()