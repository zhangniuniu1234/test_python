import threading
import time
import logging
import  _thread
logging.basicConfig(level=logging.INFO)
loops=[2,4]

class MyThread(threading.Thread):
    def __init__(self,func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)



def loop(nloop, nsec):
    logging.info("start loop "+str(nloop)+' at'+time.ctime())
    time.sleep(nsec)
    logging.info("start loop " + str(nloop)+' at'+time.ctime())




if __name__ == '__main__':
    logging.info("start all at" + time.ctime())
    nloops=range(len(loops))
    threads = []
    for i in nloops:
        t=MyThread(loop,(i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    #主线程退出，子线程强制退出
    time.sleep(6)
    logging.info("end all at"+time.ctime())