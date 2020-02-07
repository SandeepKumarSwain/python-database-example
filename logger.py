import logging
from datetime import datetime

def start():
    file_name = 'log/{}.log'.format(str(datetime.now().strftime("%H%M%S")))
    logging.basicConfig(filename=file_name, filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Started Log File')
def debug(msg):
    logging.debug(msg)
def info(msg):
    logging.info(msg)
def warning(msg):
    logging.warning(msg)
def error(msg):
    logging.error(msg)
def critical(msg):
    logging.critical(msg)