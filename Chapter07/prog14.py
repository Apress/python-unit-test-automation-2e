from loguru import logger
import sys
logger.add(sys.stdout,
           format="{time}:{level}:{message}",
           level="TRACE")
logger.trace('Trace')
logger.debug('Debug')
logger.info('Info')
logger.success('Success')
logger.warning('Warning')
logger.error('Error')
logger.critical('Critical')
