
import logging

# create logger
logger = logging.getLogger("MLApp")
logger.setLevel(logging.INFO)

#file handler
file_handler = logging.FileHandler("ml_app.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# log events
logger.info("Model loaded successfully")
logger.warning("Prediction confidence below threshold")
logger.error("Failed to process the input data")
