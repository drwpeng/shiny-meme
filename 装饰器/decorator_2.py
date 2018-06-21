

# 类装饰器
# __call__()是一个特殊方法，它可将一个类实例变成一个可调用对象
class Decorator():
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("decorator start")
        self.f()
        print("decorator end")


@Decorator
def fun():
    print("fun...")


fun()
