

# lambda的一般形式是关键字lambda，之后是一个或多个参数（与一个def头部内用括号括起来的参数列表及其相似），紧跟的是一个冒号，之后是一个表达式：

#   lambda argument1，argument2，... argumentN：expression using argument

# 由lambda表达式所返回的函数对象与由def创建并复制后的函数对象工作起来是完全一样的，但是lambda由一些不同之处让其在扮演特定的角色时很有用。


# lambda是一个表达式，而不是一个语句。
# 因为这一点，lambda能够出现在Python语法不允许def出现的地方——例如，在一个列表常量中或者函数调用的参数中。
# 此外，作为一个表达式，lambda返回了一个值（一个新的函数），可以选择性的赋值给一个变量名。
# 相反，def语句总是得在头部将一个新的函数赋值给一个变量名，而不是讲这个函数作为结果返回。


# lambda的主体是一个单个的表达式，而不是一个代码块。这个lambda的主体简单得就好像放在def主体的return语句中的代码一样。简单地将结果写成一个顺畅的表达式，而不是明确的返回。
# 因为它仅限于表达式，lambda通常要比def功能要小：你仅能够在lambda主体中封装有限的逻辑进去，连if这样的语句都不能够使用。 这是有意设计的——它限制了程序的嵌套：lambda是一个为编写简单的函数而设计的，而def用来处理更大的任务。


#            普通函数
def func(arg):
    return arg + 1

result = func(123)

#            lambda
my_lambda = lambda arg : arg + 1
result = my_lambda(123)

# 这里的f被赋值给一个lambda表达式创建的函数对象。 这也就是def所完成的任务，只不过def的赋值是自动进行的。

# 默认参数也能够在lambda参数中使用，就像在def中使用一样
x = (lambda a='fee', b='fie', c='foe': a + b + c)
print(x('wee'))
# 'weefiefoe'

# 在lambda主体中的代码想在def内的代码一样都遵循相同的作用于查找法则。lambda表达式引入的一个本地作用域更像一个嵌套的def语句，将会自动从上层函数中、模块中 以及内置作用域中（通过LEGB法则）查找变量名。
def knights():
    title = "Sir "
    action = (lambda x: title + x)
    return action

act = knights()
print(act('robin'))
# 'Sir robin'


'''
为什么使用lambda

通常来说，lambda起到了一种函数速写的作用，允许在使用的代码内嵌入一个函数的定义。他们完全是可选的（你总是能够使用def来替代它们），但是你仅需要嵌入小段可执行代码的情况下它们会带来一个更简洁的代码结构。

例如，我们在稍后会看到回调处理器，它常常在一个注册调用（registration call）的参数列表中编写成单行的lambda表达式，而不是使用在文件其他地方的一个def来定义，之后引用那个变量名。

lambda通常用来编写跳转表（jump table），也就是行为的列表或字典，能够按照需要执行相应的动作。如下段代码所示
'''
L = [lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4]

for f in L:
    print(f(2))
# 4, 8, 16

print(L[0](3))
# 9


# 每个嵌套的lambda都生成并留下了一个在之后能够调用的函数。通过键索引来取回其中一个函数，而括号使去除的函数被调用。 与在之前向你展示的if语句的扩展用法相比，这样编写代码可以使字典成为更加通用的多路分支工具。
key = 'got'
dic = {'already': (lambda: 2+2),
    'got': (lambda: 2*4),
    'one': (lambda: 2 ** 6)}
print( dic[key]() )


def cout(x):
    return lambda x, y : x + y

f = cout(3)
print( f(4) )
