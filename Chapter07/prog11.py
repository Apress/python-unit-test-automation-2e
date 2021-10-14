import logging
import threading
import time

def worker(arg, number):
    while not arg['stop']:
        logging.debug('Hello from worker() thread number '
                      + str(number))
        time.sleep(0.75 * number)

logging.basicConfig(level='DEBUG',
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
info = {'stop': False}
thread1 = threading.Thread(target=worker, args=(info, 1, ))
thread1.start()
thread2 = threading.Thread(target=worker, args=(info, 2, ))
thread2.start()
while True:
    try:
        logging.debug('Hello from the main() thread')
        time.sleep(1)
    except KeyboardInterrupt:
        info['stop'] = True
        break
thread1.join()
thread2.join()

