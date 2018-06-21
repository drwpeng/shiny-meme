

import time

def decorator1(func):
    def wrapper(self):
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper

class Method():
    @decorator1
    def fun3():
        print("fun3 running...")
        time.sleep(1)

p1 = Method()
p1.fun3()
