import time
from threading import Thread


def do_job(number, second_arg=None):
    for i in range(10):
        print(f'From child thread: {i}, {number}, {second_arg}')
        time.sleep(0.2)


thread = Thread(target=do_job, args=(1,), kwargs={'second_arg': 56})
thread.start()

for i in range(10, 20):
    print(f'From main thread: {i}')
    time.sleep(0.1)