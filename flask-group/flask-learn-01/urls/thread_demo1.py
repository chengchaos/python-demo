# -*- coding:utf-8 -*-
import _thread
import time


# Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
# _thread 提供了低级别的、原始的线程以及一个简单的锁，相比较 threading 模块功能有限。
# threading 除了包含 _thread 模块的方法，还提供了：
# - threading.currentThread(): 返回当前的线程变量。
# - threading.enumerate(): 返回一个包含正在运行的线程的 list。（正在运行指线程启动后、结束前，不包括启动前和终止后的线程。）
# - threading.activeCount(): 返回正在玉兴的线程的数量。（与len(threading.enumerate())有相同的结果。）
# 使用函数或者类名来包装对象线程：
# _thread.start_new_thread(function, args[, kwargs])
# 定义一个线程函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s : %s " % (thread_name, time.ctime(time.time())))


if __name__ == "__main__":
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 3,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass
