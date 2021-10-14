from loguru import logger

logger.add('mylog.log',
           backtrace=True,
           diagnose=True)

def function1(a, b):
    return a / b

def function2(c):
    try:
        function1(5, c)
    except ZeroDivisionError:
        logger.exception('Divide by Zero!')

function2(0)
