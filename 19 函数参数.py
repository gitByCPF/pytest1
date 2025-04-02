# 函数参数
# 1. 必备参数（位置参数）：传递和定义参数的顺序和个数必须一致
# 2. 默认参数（缺省参数）：为参数提供默认值，调用参数时可不传该默认参数的值，必须位于必备参数之后
def fun_a(a=8):
    print(a)


fun_a()
# 实参的优先级高于默认值
fun_a(2)


# 不允许默认参数在必备参数之前
# def fun_b(a=2, b):
#     print(a, b)

# 3. 可变参数：传入的值的数量是可变的，可以不传,可以传入多个，以元组形式接收
def fun_c(*args):
    print(args)
    print(type(args))


fun_c(1, 2, 3)

# 4. 关键字参数：以字典的形式接受，以键值对的形式传值
def fun_d(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun_d()
fun_d(name='John', age=20)

