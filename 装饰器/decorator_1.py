

import time

# 装饰器
# 让其他函数在不需要做任何代码变动的前提下增加额外功能
# 经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景


# 不带参数的装饰器
def decorator1(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("不带参数的装饰器: " + str(end_time - start_time))
    return wrapper


# 带参数的装饰器 
def decorator2(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        print("带参数的装饰器: " + str(end_time - start_time))

    return wrapper


# 带不定参数的装饰器 
def decorator3(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("带不定参数的装饰器: " + str(end_time - start_time))

    return wrapper


# 函数的函数装饰器 
@decorator1
def fun():
    print("sleeping...")
    time.sleep(1)

@decorator2
def fun2(a, b):
    print("a + b = " + str(a+b))
    time.sleep(1)


# 用于类的不带参数的装饰器
def decorator4(func):
    def wrapper(self):
        start_time = time.time()
        func()
        end_time = time.time()
        print("不带参数的装饰器: " + str(end_time - start_time))
    return wrapper

# 用于类的带参数的装饰器
def decorator5(func):
    def wrapper(self):
        start_time = time.time()
        func(self)
        end_time = time.time()
        print("不带参数的装饰器: " + str(end_time - start_time))
    return wrapper

# 用于类的带参数的装饰器
def decorator6(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("不带参数的装饰器: " + str(end_time - start_time))
    return wrapper


# 类方法的函数装饰器
class Method():
    #def __init__(self):
        #print("locker.__init__() should be bot called")

    @decorator4
    def fun3():
        print("Running...")
        time.sleep(1)

    @decorator5
    def fun4(self):
        pass

    @decorator6
    def fun5(*args, **kwargs):
        pass

p1 = Method()
p1.fun3()
p1.fun4()
p1.fun5()
