import time
import _thread


def task2():
    while True:
        print("123")
        time.sleep_ms(2001)


_thread.start_new_thread(task2, ())

while True:
    time.sleep_ms(2000)