import numpy as np
import threading
import time

def waste_time():
    a = np.ones((100,100,100))
    b = np.ones((100,100,100))
    _ = np.dot(a,b)
    return _
    
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global n
        waste_time()
        # print (n , self.name)
        n += 1

start = time.time()
n = 1
ThreadList = []
for i in range(1, 5):
    t = MyThread()
    ThreadList.append(t)
for t in ThreadList:
    t.start()
for t in ThreadList:
    t.join()
print('time consumed: ', time.time()-start)
