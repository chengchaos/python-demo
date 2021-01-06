# -*- coding:utf-8 -*-
import threading
import time

exit_flag = 0


# https://www.runoob.com/python3/python3-multithreading.html
#
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：", self.name)
        print_time(self.name, self.counter, 5)
        print("结束线程：", self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1


if __name__ == "__main__":
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    thread2.join()
    thread2.join()

    print("-- end --")
