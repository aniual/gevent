import threading as th
from time import sleep

i = 1
e = th.Event()

def bar():
    global i
    i = 'i miss you'
    print('huhu')


def foo():
    print('wait i...')
    sleep(2)
    print('foo %s' % i)
    e.set()


def fun():
    sleep(1)
    e.wait()
    print('hehe')
    global i
    i = 'i hate you'


t1 = th.Thread(name='bar', target=bar)
t2 = th.Thread(name='foo', target=foo)
t3 = th.Thread(name='fun', target=fun)
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
