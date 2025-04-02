import builtins

# 大写字母开头，一般是内置常量名；小写字母开头，一般是内置函数名
# names = dir(builtins)
# const_names = list(filter(lambda x: x[0].isupper(), names))
# func_names = list(filter(lambda x: x.islower() & (not x.startswith("_")), names))
# magic_func_names = list(filter(lambda x: x.startswith('_'), names))
# print(const_names)
# print(func_names)
# print(magic_func_names)

print(sum({1, 2, 4, 6, 8}))
print(sum([1, 2, 4, 6, 8]))
print(sum((1, 2, 4, 6, 8)))

l1 = [1, 2, 4, 6, 8]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = ['北', '京', '欢', '迎', '您']
# zip将可迭代对象作为参数，将可迭代对象打包成一个个元组，以最短的迭代对象为数量
print(list(zip(l1, l2, l3)))

# map(func, iterable)映射可迭代对象中的每个元素，并逐个带入执行函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

# reduce(func, sequence, initial)
# 用于累积计算，依次对 iterable 的元素应用 function，将其缩减为单一值
# sequence与initial不能同时为空
from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 2))
print(reduce(lambda x, y: x * y, [], 2))

# 拆包
# 方法一：用对应数量的变量接受可迭代对象中的元素值
tpl = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
a, b, c = tpl
print(a, b, c)
print(type(a), type(b), type(c))

# 方法二：可变变量接收多个元素，与可迭代对象数据类型保持一致
tpl = [1, 2, 3, 4, 5]
a, *b, c = tpl
print(a, b, c)
print(type(a), type(b), type(c))
