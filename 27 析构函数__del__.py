# __del__
# 删除对象的时候，解释器会默认调用__del__()方法
#
class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('__init__')

    def __del__(self):
        print('__del__')

p = Person('jack')
print('执行代码')

print(dir(object))
