# 单例模式：特殊的类，只允许存在一个对象
# 优点：节省内存空间，减少资源浪费
# 缺点：多线程访问时候，竞争激烈
"""
实现方式：
1.重写__new__()方法             ok
2.通过导入模块实现              ok
3.通过@classmethod实现
    也就是写个方法，每次获取的是同一个实例而已，无法阻止初始化新的实例
4.通过装饰器实现
"""

# 方式一
class One(object):
    obj = None

    def __new__(cls):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

o1 = One()
print(id(o1))
o2 = One()
print(id(o2))

# 方式二
from singleton import te as test1
from singleton import te as test2
print(id(test1))
print(id(test2))

# 方式四：装饰器
# 拓展：不仅可以装饰方法去丰富功能，也能装饰类来限制实例化
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
# MyClass = singleton(MyClass) = wrapper
# MyClass(value) = singleton(Myclass)(value) = wrapper(value) = instances[cls]
class MyClass(object):
    def __init__(self, value):
        self.value = value

a = MyClass(1)
b = MyClass(2)
print(a is b)
print(a.value)
print(b.value)
print(id(a))
print(id(b))
