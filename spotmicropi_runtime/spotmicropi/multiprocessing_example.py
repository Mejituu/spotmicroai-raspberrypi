#!/usr/bin/env python3

import multiprocessing
import time


class MyFancyClass(object):

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Doing something fancy in %s for %s!' % (proc_name, self.name))


def worker(q):
    while True:
        # obj = q.get()
        # obj.do_something()
        q.put(MyFancyClass('Fancy child 1a'))
        q.put(MyFancyClass('Fancy child 1b'))
        q.put(MyFancyClass('Fancy child 1c'))
        q.put(MyFancyClass('Fancy child 1d'))
        q.put(MyFancyClass('Fancy child 1e'))
        time.sleep(1 / 5)


def worker2(q):
    while True:
        # obj = q.get()
        # obj.do_something()
        q.put(MyFancyClass('Fancy child 2a'))
        q.put(MyFancyClass('Fancy child 2b'))
        q.put(MyFancyClass('Fancy child 2c'))
        q.put(MyFancyClass('Fancy child 2d'))
        q.put(MyFancyClass('Fancy child 2e'))
        time.sleep(1 / 5)


if __name__ == '__main__':
    queue = multiprocessing.Queue(2)

    p1 = multiprocessing.Process(target=worker, args=(queue,))
    p1.daemon = True
    p1.start()

    p2 = multiprocessing.Process(target=worker2, args=(queue,))
    p2.daemon = True
    p2.start()

    while True:
        # queue.put(MyFancyClass('Fancy Parent'))
        obj = queue.get()
        obj.do_something()
        time.sleep(1 / 2)

    # Wait for the worker to finish
    queue.close()
    queue.join_thread()
    p.join()
