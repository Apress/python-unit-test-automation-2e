from loguru import logger
import sys
logger.add("mylog_{time}.log",
           format="{time}:{level}:{message}",
           level="TRACE")
new_level = logger.level("OKAY", no=15, color="<green>")
logger.trace('Trace')
logger.debug('Debug')
logger.log("OKAY", "All is OK!")
logger.info('Info')

