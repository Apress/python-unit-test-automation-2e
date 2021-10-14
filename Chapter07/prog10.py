import logging
logger1 = logging.getLogger('Logger1')
logger1.setLevel(logging.DEBUG)
logger2 = logging.getLogger('Logger2')
logger2.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
ch.setFormatter(console_formatter)
logger1.addHandler(ch)


fh = logging.FileHandler('mylog.log',
                         encoding='utf-8')
fh.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(file_formatter)
logger2.addHandler(fh)


logger1.debug('Debug')
logger2.debug('Debug')
logger1.info('Info')
logger2.info('Info')
logger1.warning('Warning')
logger2.warning('Warning')
logger1.error('Error')
logger2.error('Error')
logger1.critical('Critical')
logger2.critical('Critical')
