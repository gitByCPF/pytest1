# 类方法
class Person(object):
    @classmethod
    def sleep(cls):
        print(cls)
        print("sleep")

Person.sleep()
print(Person)
