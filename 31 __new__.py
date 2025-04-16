# 单例模式
# __new__由object基类提供的内置的静态方法
# 作用一：在内存中为对象分配空间
# 作用二：返回对象的引用
# __init__()初始化对象，没有__new__创建的对象，就没有初始化方法
class Person(object):
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)

    def __init__(self):
        self.name = "person"
        print("__init__")

person = Person()
print(person.name)
