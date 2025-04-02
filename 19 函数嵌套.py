# 嵌套定义：在一个函数内定义另一个函数
def study():
    print("welcome to study")
    def course():
        print("math")
    course()

study()

