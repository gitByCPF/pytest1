# 多继承：子类可以拥有多个父类，并且具有所有父类的属性和方法
# 如果多个父类拥有同名方法，以就近原则继承，即写在继承括号前面的先继承
# py中内置的属性__mro__可以查看方法搜索顺序
# 多继承容易引发冲突，代码设计复杂性增加
class Father(object):
    def money(self):
        print('Father money')

class Mother(object):
    def appearance(self):
        print('Mother appearance')

    def money(self):
        print('Mother money')

class Child(Father,Mother):
    pass

class Son(Mother,Father):
    pass

child = Child()
son = Son()

child.appearance()

child.money()
son.money()

print(Child.__mro__)
print(Son.__mro__)