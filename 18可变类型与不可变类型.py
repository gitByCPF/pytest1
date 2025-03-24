# 可变类型：变量对应的值可以改变，但是对象地址不会发生改变
# dict list set 是可变类型

# 不可变类型：存储空间保存的数据不允许修改
# 数值类型 字符串 tuple 都是不可变类型
n = 1
print(id(n))
n = 2
print(id(n), end="\n\n")

s = "hello"
print(id(s))
s = s + " world"
print(id(s), end="\n\n")

tp = (1, 2, 3)
print(id(tp))
tp = (1, 2, 3, 4)
print(id(tp), end="\n\n")
