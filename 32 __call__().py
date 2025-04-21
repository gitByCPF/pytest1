# 如果一个对象实现了 __call__() 方法，那么它就可以像函数一样被调用！
# __call__() 的设计目的是为了让对象“行为上像函数”，让类的实例“可调用”，支持函数式编程风格
# 应用场景
# 1.状态保持函数,调用时直接是c()而不是c.count()
class Counter(object):
    def __init__(self):
        self.value = 0

    def __call__(self):
        self.value += 1
        return self.value


counter = Counter()
print(counter())
print(counter())
print(counter())


# 2.装饰器实现
""" 经典方式
def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"函数{func.__name__} 开始执行，参数{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"函数{func.__name__} 执行完毕，返回值{result}")
        return result

    return wrapper

@decorator
def greet(name):
    print('Hello ' + name)

greet('John')
"""
class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"函数{self.func.__name__} 开始执行，参数 {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"函数{self.func.__name__} 执行完毕，返回值 {result}")
        return result

@Decorator
# greet = Decorator(greet) = decorator
# greet(name) = decorator(name) = __call__(name)
def greet(name):
    print('Hello ' + name)

greet('John')






















