from loguru import logger
import sys

logger.add(sys.stdout,
           colorize=True,
           format="<blue>{time}</blue> <level>{message}</level>")

logger.add('mylog.log',
           format="{time:YYYY-MM-DD @ HH:mm:ss} - {level} - {message}")

logger.debug('Debug')
logger.info('Info')
