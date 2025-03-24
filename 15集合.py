# 集合名 = {元素1,元素2...}
# 1.集合具有无序性，每次打印结果都不一样
# 集合的无序性，基于hash值来实现的，因此hash不稳定的数据，每次集合输出的顺序会改变
# 可变数据类型(字典、列表、集合)是不能hash的，tuple string bytes是不稳定的，只有int float是稳定的
s = {1, 2.0, b'hello', (3, 4), "str"}
# 因此，该集合输出，除了1 2.0的顺序保持一致，其它都是随机
print(s)

# 2.集合具有唯一性
# 即使加入重复元素，也能自动去重
s.add(1)
print(s)

# 拆分添加 拆分的必须是可迭代对象
# s.update(10)
s.update("new")
s.update({8, 9})
print(s)

# 常见操作
if 2.0 in s:
    print("2.0 exist")
# 删除时候不存在会报错
s.remove(8)
print(s)

# 同一个集合，在同一个进程中的顺序是一致的
print({'1', 2, '3', 4, '5', 6}.pop())
print({'1', 2, '3', 4, '5', 6}.pop())
# 因为同一个进程中，即使不稳定数据的hash值也是一致的
print(hash('1'))
print(hash('1'))

# discard 丢弃元素，不存在也不会报错
# 返回值永远是None
print(s.discard("not_exist"))
print(s.discard(b'hello'))
print(s)

# 交集
print({1, 2, 3, 4} & {3, 4, 5, 6})
# 没有交集，返回空集合set()
print({1, 2, 3, 4} & {5, 6, 7, 8})
# 并集
print({1, 2, 3, 4} | {3, 4, 5, 6})
# 并集方法
print({1, 2, 3, 4}.union({3, 4, 5, 6}))
