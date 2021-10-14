import logging
logging.basicConfig(filename='logfile.log',
                    encoding='utf-8',
                    level=logging.DEBUG)
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')
