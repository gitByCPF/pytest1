# 静态方法
# 既可以使用类名调用，也可以使用对象调用
# 取消不必要的参数传递，减少内存消耗和性能销号

class Person(object):
    name = '人类'

    @staticmethod
    def study():
        print("会学习")

    @classmethod
    def read(cls):
        print("读书能进步")

Person.study()
p = Person()
p.study()
