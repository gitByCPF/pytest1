"""
__new()__先被调用，返回一个实例化对象
__init()__后调用，初始化该对象的属性值
注意！如果__new()__返回的不是当前类的实例，__init()__就不会被调用
子对象实例化时候，是先调用子辈构造函数，再调用父辈
"""
class A:
    def __new__(cls, *args, **kwargs):
        print("👷 A __new__ 被调用")
        return super().__new__(cls)

    def __init__(self, *args):
        print("🎯 A __init__ 被调用")
        self.class_name = 'A'


class B(A):
    def __new__(cls, *args, **kwargs):
        print("👷 B __new__ 被调用")
        return super().__new__(cls)

    def __init__(self, *args):
        print("🎯 B __init__ 被调用")
        super().__init__(*args)
        self.class_name = 'B'


class C(B):
    def __new__(cls, *args, **kwargs):
        print("👷 C __new__ 被调用")
        return super().__new__(cls)

    def __init__(self, *args):
        print("🎯 C __init__ 被调用")
        super().__init__(*args)
        self.class_name = 'C'

obj = C()
