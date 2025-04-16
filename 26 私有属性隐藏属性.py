# 面向对象：封装、继承、多态
# 封装： 隐藏对象中不希望被外部所访问到的属性和方法
class Person:
    name = 'Jack'
    _gender = 'male'
    # 属性名或者方法名以__开头命名，仅能在类内被访问到
    __age = 28

    def introduce(self):
        print(f'{Person.name}的年龄是{Person.__age}')


print(Person.name)
print(Person._gender)
# print(Person.__age)
# 但其实内部只是改了一个名字，在外部仍然能够访问到并且修改
print(Person._Person__age)
Person._Person__gender = 'female'
print(Person._Person__gender)

pe = Person()
pe.introduce()
