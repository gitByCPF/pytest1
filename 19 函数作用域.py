# 函数内部如果要使用变量，先找局部变量，再找全局变量
# 同名的局部变量的改变，无法影响全局变量
# 如果需要在局部修改或者声明一个全局变量，要用到global关键字，先声明，后使用
a = 100


def local1():
    global a
    a += 1


local1()
print(a)


def local2():
    global b, c
    b = 1
    c = 2


def local3():
    print(b)
    print(c)


# 声明全局变量的函数必须先执行，全局变量才能被后面执行的函数察觉到
local2()
local3()

print("*********************")

# nonlocal 用于在 嵌套函数 内修改 最近的外层（非全局）作用域 变量，而不创建新的局部变量
o = 1


def outer():
    o = 2
    print("outer中o=", o)
    def inner1():
        print("inner1中o=", o)
        def inner2():
            nonlocal o
            o = 3
        inner2()
        print("inner2修改后o=", o)
    inner1()
    print("inner2修改后outer中的o=", o)

outer()
