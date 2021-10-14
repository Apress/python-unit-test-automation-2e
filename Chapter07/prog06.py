import logging
logging.basicConfig(filename='logfile.log',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG)
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')
