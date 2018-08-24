import threading as th
import random as rm
from time import sleep

a = 500

# 创建事件对象
e = th.Event()

# 子线程不断减少a,但是希望a的值不会少于100
def fun():
    global a
    while True:
        sleep(2)
        print(a)
        e.wait()
        a -= rm.randint(0, 100)


t = th.Thread(name='fun', target=fun)
t.start()
# 主线程不断的让a增加以确保a不会小于100
while True:
    sleep(1)
    a += rm.randint(1, 10)
    if a > 100:
        e.set()
    else:
        e.clear()

t.join()
