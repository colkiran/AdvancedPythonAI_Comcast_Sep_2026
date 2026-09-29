
import logging

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("app.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# app/ database.py
db_logger = logging.getLogger("app.database")
db_logger.debug("Connection to the database......")

# app/ api.py
db_logger = logging.getLogger("app.api")
db_logger.info("Received request from client.....")