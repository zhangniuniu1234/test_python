import time
import logging
import  _thread
logging.basicConfig(level=logging.INFO)
loops=[2,4]
def loop0():
    logging.info("start loop0"+time.ctime())
    time.sleep(4)
    logging.info("start loop0" + time.ctime())

def loop1():
    logging.info("start loop1"+time.ctime())
    time.sleep(2)
    logging.info("start loop1" + time.ctime())

if __name__ == '__main__':
    logging.info("start all at" + time.ctime())
    _thread.start_new(loop0, ())
    _thread.start_new(loop1, ())
    #主线程退出，子线程强制退出
    time.sleep(6)
    logging.info("end all at"+time.ctime())