import threading as th
from time import sleep

a = b = 0
lock = th.Lock()

def value():
    while True:
        lock.acquire()
        if a != b:
            sleep(1)
            print('a = %d,b=%d'%(a,b))
        lock.release()



t = th.Thread(target=value)
t.start()
while True:
    lock.acquire()
    a += 1
    b += 1
    lock.release()

t.join()