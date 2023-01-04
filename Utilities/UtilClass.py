import logging
import inspect


class utils:

    def get_logger(self, log_level=logging.debug()):
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        file_handler = logger.FileHandler("automation.log")
        formatter = logging.Formatter("%(asctime)s:%(levelname)s - %(name)s : %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
