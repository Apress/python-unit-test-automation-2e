from loguru import logger
import sys

config = {
    'handlers': [
        {'sink': sys.stdout, 'format': '{time} - {message}'},
        {'sink': 'mylog.log', 'serialize': True}]
}

logger.configure(**config)

logger.debug('Debug')
logger.info('Info')
