"""
一个程序运行起来至少一个进程，一个进程至少有一个线程
进程是操作系统分配程序执行资源的单位，线程是进程的一个实体是CPU调度和分配的单位，其中CPU执行方式为时间片轮训方式，
线程自己基本上不拥有系统资源,但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.
主线程会等待所有子线程结束才结束
多线程共享全局变量，且多线程对同一个全局变量操作时会出现资源竞争问题导致数据不准确，使用互斥锁解决; 多进程不共享全局变量
程序中使用多个锁，相互依赖会造成死锁
并发：交替处理多个任务的能力 并行：同时处理多个任务的能力
GIL：全局解释器锁，保证同一时刻只有一个线程能执行代码，但是由于IO操作的存在所以多线程比单线程一般会更快除非是处理科学计算多线程反而会慢


threading.enumerate() 枚举当前所有线程

互斥锁
mutex = threading.Lock()
mutex.acquire()
mutex.release()

os.getpid() 获取当前进程id
os.getppid() 获取当前进程父进程的id

Queue().qsize() 返回队列消息数量
Queue().empty() 判断队列是否为空
Queue().full() 判断队列是否为满
Queue().get() 获取队列消息，可设置阻塞或不阻塞以及阻塞时间
Queue().get_nowait() 不等待获取队列消息
Queue().put() 插入队列消息，可设置阻塞或不阻塞以及阻塞时间
Queue().put_nowait() 不等待获取队列消息

进程池使用队列时必须用Manager中的队列，多进程使用队列直接用Queue，混用会出现异常

可迭代对象：具有__iter__方法的对象就是可迭代对象，正常的__iter__方法需返回迭代器
迭代器：具有__iter__方法和__next__方法的对象，__iter__方法一般指向自身，所以迭代器一定是可迭代对象。
外界可通过iter()函数调用可迭代对象的__iter__方法获取迭代器，next()方法调用迭代器的__next__方法来依次获取数据,
这同样是for循环的实质

具有yield关键字的函数都是生成器，yield可以理解为return，返回后面的值给调用者。
不同的是return返回后，函数会释放，而生成器则不会。在直接调用next方法或用for语句进行下一次迭代时，生成器会从yield下一句开始执行，直至遇到下一个yield。

协程进化史：
协程是单线程并发
1.使用yield和next实现程序切换
2.使用greenlet封装协程代码，switch实现程序切换
3.使用gevent封装协程代码，自动切换程序。需要通过monkey来封装耗时操作才能在不改变程序代码的情况下实现协程切换
"""

import threading
from multiprocessing import Process, Queue, Pool, Manager
import time
import os
import random
import gevent
from gevent import monkey
monkey.patch_all()


class CustomThread(threading.Thread):
    """
    定义子类继承threading.Thread并重写run方法，可以对多线程进行封装
    """
    def run(self):
        for i in range(5):
            time.sleep(1)  # 休眠1秒
            print("---正在下载歌曲%d---" % i)


def write(queue, age, num=None):
    """写"""
    print("接受参数%s, %s" % (age, num))
    print("--write--子进程的父进程的id=%d   子进程的id= %d" % (os.getppid(), os.getpid()))
    for value in ["A", "B", "C"]:
        queue.put(value)


def read(queue):
    """读"""
    while queue.qsize():
        time.sleep(random.random())
        print('Get %s from queue.' % queue.get())


def pool_work(work_num, queue):
    """进程池进程工作"""
    print("任务编号：%d" % work_num)
    queue.put("任务%d已完成" % work_num)


class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, length):
        self.length = length
        self.current = 0
        self.num1 = 0
        self.num2 = 1

    def __next__(self):
        if self.current < self.length:
            res = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return res
        else:
            # 必须要写，否则会无限迭代
            raise StopIteration

    def __iter__(self):
        return self


def fib(length):
    """斐波那契数列生成器"""
    current = 0
    num1, num2 = 0, 1
    while current < length:
        message = yield num1
        print(message)
        num1, num2 = num2, num1 + num2
        current += 1


def coroutine_work(work_no, cycle_index):
    """协程任务"""
    for i in range(cycle_index):
        print("%s模拟IO操作：%d" % (work_no, i), gevent.getcurrent())
        time.sleep(1)


def main():
    """主函数"""
    # t1 = CustomThread()
    # t1.start()
    # print(threading.enumerate())
    # print("--main--主进程的父进程id=%d   主进程的id= %d" % (os.getppid(), os.getpid()))
    # queue = Queue(10)
    # pw = Process(target=write, args=(queue, 18), kwargs={"num": 20})
    # pw.start()
    # pw.join()
    # pr = Process(target=read, args=(queue,))
    # pr.start()
    # pool = Pool(3)
    # queue = Manager().Queue(10)
    # for work_num in range(10):
    #     # 无论任务数量是否多余pool的最大值，都不阻塞主进程
    #     pool.apply_async(pool_work, (work_num, queue))
    # # 不再接受新的请求，不包括排队中的任务
    # # pool.terminate()可以强制停止执行中的任务
    # pool.apply_async(read, (queue,))
    # pool.close()
    # # 等待pool中所有子进程执行完成，必须放在close语句之后
    # pool.join()
    # fib = FibIterator(10)
    # for num in fib:
    #     print("  ", num, end="")
    # gen = fib(10)
    # print(next(gen))
    # print(gen.send("xiong"))
    gevent.joinall([gevent.spawn(coroutine_work, "work1", 5),
                    gevent.spawn(coroutine_work, "work2", 7)])


if __name__ == '__main__':
    main()
