# 继承：子类默认继承父类所有的自定义属性和方法
# class Son(Father):
# 子类可以继承父类以及上溯所有父类的方法和属性
# 子类可以重写父类的方法

class Person:
    _age = 50
    __money = 100000

    def eat(self):
        print('eat')

    def sing(self):
        print('sing')


class Girl(Person):
    # 占位符，类下面不写任何东西，会自动跳过，不会报错
    pass


girl = Girl()
girl.eat()
girl.sing()

# 私有属性正常继承
print(girl._age)
# 隐藏属性以魔改后的名字继承
print(girl._Person__money)

class Boy(Person):
    def eat(self):
        # super是一个特殊的类，表示当前类的父类
        super().eat()
        print('i eat a lot')

boy = Boy()
boy.eat()
