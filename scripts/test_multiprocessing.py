import numpy as np
import multiprocessing
import time


def waste_time():
    a = np.ones((100,100,100))
    b = np.ones((100,100,100))
    _ = np.dot(a,b)
    return _



class imreg_thread(multiprocessing.Process):
    
    def run(self):
        # print('entering a new process...')
        global n
        waste_time()
        # print('inside lock, process number:', self.name)

start = time.time()
n = 1
ProcessList = []
for i in range(1, 2):
    t = imreg_thread(name=i)
    ProcessList.append(t)
for t in ProcessList:
    t.start()
for t in ProcessList:
    t.join()
print('time consumed: ',time.time()-start)
