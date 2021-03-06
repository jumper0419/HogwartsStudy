# -*- coding: UTF-8 -*-

import threading
import time


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print_time(self.name, self.delay)



def print_time(name, delay):
    print("Starting " + name + "ctime: " + time.ctime(time.time()))
    time.sleep(int(delay))
    print("Exiting " + name + "ctime: " + time.ctime(time.time()))


def main(m, n , t):
    print("Starting Main Thread")
    task_handle_time_list = t.split()
    task_handle_time_list.sort()
    # print(task_handle_time_list)
    threads = []
    delay_index = 0
    # 创建新线程
    for i in range(n):
        delay_time = int(task_handle_time_list[delay_index])
        thread = myThread(i, f"Thread-{i}", f"{delay_time}")
        threads.append(thread)
        delay_index += 1
    for i in range(m):
        # 开启线程
        threads[i].start()
    for t in threads:
        t.join()
        # print(len(threads))
    print(len(threads))
    print("Exiting Main Thread")

if __name__ == "__main__":
    m, n = 3, 5
    t = "8 4 3 1 1 0"
    main(m, n , t)