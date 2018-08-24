import threading as th
from time import ctime, sleep


def music(sec):
    print('Listening music')
    sleep(sec)


t = th.Thread(name='my thread', target=music, args=(2,))
t.start()


print('创建线程 ')
