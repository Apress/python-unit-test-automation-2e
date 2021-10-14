import logging
import logging.handlers

logfile = 'mylog.log'
logger = logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)

rfh = logging.handlers.RotatingFileHandler(logfile,
                                           maxBytes=10,
                                           backupCount=5)
rfh.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rfh.setFormatter(file_formatter)
logger.addHandler(rfh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
ch.setFormatter(console_formatter)
logger.addHandler(ch)

logger.debug('Debug')
logger.info('Info')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')
