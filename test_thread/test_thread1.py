import time
import logging
import  _thread
logging.basicConfig(level=logging.INFO)
loops=[2,4]
def loop(nloop, nsec, lock):
    logging.info("start loop0"+str(nloop)+'at'+time.ctime())
    time.sleep(nsec)
    logging.info("start loop0" + str(nloop)+'at'+time.ctime())
    lock.release()



if __name__ == '__main__':
    logging.info("start all at" + time.ctime())
    locks = []
    nloops=range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked(): pass
    #主线程退出，子线程强制退出
    time.sleep(6)
    logging.info("end all at"+time.ctime())