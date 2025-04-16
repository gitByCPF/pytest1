# 多态：同一种行为具有不同的表现形式
# 多态的前提：继承、重写
class Animal(object):
    """父类：动物类"""
    def shout(self):
        print('动物会叫')

class Dog(Animal):
    def shout(self):
        print("小狗汪汪汪")

class Cat(Animal):
    def shout(self):
        print("小猫喵喵喵")

def test(obj):
    obj.shout()

test(Animal())
test(Cat())
test(Dog())

