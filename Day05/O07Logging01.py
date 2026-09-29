
import logging

# configure logging, default level - warnings
logging.basicConfig(
    level=logging.DEBUG, # captures all levels from DEBUG upwards
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debugging details variable x = 54")
logging.info("Application Started Successfully")
logging.warning("Low disk space detected")
logging.error("Database connection failure")
logging.critical("System crashed due to insufficient memory to continue execution of the program")