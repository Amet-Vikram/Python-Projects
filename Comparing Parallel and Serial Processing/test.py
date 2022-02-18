import cv2
import multiprocessing
import threading
import numpy as np
import time


 
#read image
src = cv2.imread('Galaxy.jpg', cv2.IMREAD_UNCHANGED)

#view the shape of array
#print(type(src))

def split_ch(src):
    b,g,r = np.zeros(src.shape), np.zeros(src.shape), np.zeros(src.shape)
    b[:,:,0],g[:,:,1],r[:,:,2] = cv2.split(src)
    cv2.imwrite("Model Blue Image mp.png", b)
    cv2.imwrite("Model Green Image mp.png", g)
    cv2.imwrite("Model Red Image mp.png", r)
    pass

def split_ch2(src):
    b,g,r = np.zeros(src.shape), np.zeros(src.shape), np.zeros(src.shape)
    b[:,:,0],g[:,:,1],r[:,:,2] = cv2.split(src)
    cv2.imwrite("Model Blue Image.png", b)
    cv2.imwrite("Model Green Image.png", g)
    cv2.imwrite("Model Red Image.png", r)
    pass

def split_ch3(src):
    b,g,r = np.zeros(src.shape), np.zeros(src.shape), np.zeros(src.shape)
    b[:,:,0],g[:,:,1],r[:,:,2] = cv2.split(src)
    cv2.imwrite("Model Blue Image th.png", b)
    cv2.imwrite("Model Green Image th.png", g)
    cv2.imwrite("Model Red Image th.png", r)
    pass

def concurrency():
    print ('Concurrent MP Started')
    # creating processes
    p1 = multiprocessing.Process(target=split_ch, args=(src, ))
    # start process 1
    p1.start()

    """print ("waiting 3 secs for process to start")
    time.sleep(3) # Wait for processes to start.  See Barrier in Python 3.2+ for a better solution.
    print ('Concurrent Started')
    """

    start_time = time.time()
    # wait until process 1 is finished
    p1.join()
    print("--- %s seconds in Cocurrent Multi-Processing Process ---" % (time.time() - start_time))
    pass


def non_cocurrency():
    print ('Non Cocurrent Started')
    start_time = time.time()
    split_ch2(src)
    print("--- %s seconds in Non Cocurrent Process ---" % (time.time() - start_time))
    pass

def con_thread():
    print ('Concurrent MT Started')
    t1 = threading.Thread(target=split_ch3, args=(src, ))
    t1.start()

    start_time = time.time()
    t1.join()
    print("--- %s seconds in Cocurrent Multi-Threaded Process ---" % (time.time() - start_time))
    pass


#split_ch(src)

if __name__ == "__main__":
    concurrency()
    non_cocurrency()
    con_thread()
    print ("Test Over")
    