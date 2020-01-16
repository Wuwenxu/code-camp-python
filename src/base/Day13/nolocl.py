import threading
from threading import Thread
import time

thnum = 0


class MyThread(threading.Thread):
    def run(self):
        for i in range(10000):
            global thnum
            thnum += 1
        print(thnum)


def test():
    global thnum
    for i in range(10000):
        thnum += 1
    print(thnum)


if __name__ == '__main__':
    t = MyThread()
    t.start()

time.sleep(4)  # 保证第一个线程执行完,这样的话运行结果为20000
# 但是如果将这句话屏蔽掉的话，就会发现结果不是20000，全局变量的值在其中有交叉，而不是先运行完第一个程序再运行第二个程序
thn = Thread(target=test)
thn.start()

