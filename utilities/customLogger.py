import inspect
import logging
class LogGen:

    @staticmethod
    def log_gen():
        logs_file_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject5\\Logs\\sausedemo.log"
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler(logs_file_path)
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s ", datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger




