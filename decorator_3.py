

# 装饰器链
#　　一个python函数也可以被多个装饰器修饰,
#   多个装饰器执行的顺序就是从第一个装饰器开始，执行到最后一个装饰器，再执行函数本身。 


def decorator_a(func):
    return lambda: "<a> " + func() + " </a>"

def decorator_b(func):
    return lambda: "<b> " + func() + " </b>"

def decorator_c(func):
    return lambda: "<c> " + func() + " </c>"

@decorator_a
@decorator_b
@decorator_c
def say():
    return "hello..."
    #print("hello...")

print(say())
