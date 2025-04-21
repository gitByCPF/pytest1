# 魔法方法&魔法属性
class Person(object):
    """魔法属性__doc__"""

    @staticmethod
    def sing():
        """docstring for sing"""
        print("sing")


print(Person.__doc__)
print(Person.sing.__doc__)

# __module__:表示当前操作对象所在的模块
# __class__:表示当前操作对象所在的类
import common
a = common.A()
print(a.__module__)
print(a.__class__)
# 通过当前操作对象所在的类，再创建一个对象
# print(a.__class__())

# __str__() 打印对象时，优先输出该函数的返回值，返回值必须是字符串类型，否则会报错
# 没有定义该函数的话，
class B(object):
    def __str__(self):
        return "B's __str__()"

b = B()
print(b)
print(dir(b))

# __del_()析构函数，回收对象时候被调用


