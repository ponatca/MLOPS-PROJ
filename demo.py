# below code is to check the logging config
# from mlops_proj.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
from mlops_proj.logger import logging
from mlops_proj.exception import MyException
import sys

try:
    a = 1+ 'Z' # type: ignore
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

# from mlops_proj.pipline.training_pipeline import TrainPipeline

# pipline = TrainPipeline()
# pipline.run_pipeline()