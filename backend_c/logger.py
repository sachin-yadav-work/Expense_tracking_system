import logging

def get_logger(log_name,file_name,level = logging.DEBUG,):
    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    log_handler = logging.FileHandler(file_name)
    log_handler.setLevel(level)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(log_format)
    logger.addHandler(log_handler)
    return logger