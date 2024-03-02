import inspect
import logging


class Logging_Class:
    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\girish kadam\\Desktop\\Binder\\Logs\\Amazon_Logfile.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger