# """
# 列表名 = [1,2,3,4,5,6,7,8,9]
# 1.元素的数据类型可以不同
# 2.列表也可以切片操作
# """
# l = [1, "2", [3], 4.0]
# """ 增 """
# # 尾部附加元素
# l.append('append')
# print(l)
# # 先拆分，再尾部附加
# l.extend("extend")
# # 一定要是可迭代对象
# # l.extend(1) # 会报错
# print(l)
# # insert下标超出范围，默认在头尾附加
# l.insert(len(l), "insert")
# l.insert(-100, "-100")
# print(l)
# l.insert(100, "100")
# print(l)
# # 插入中间的话，后面的元素右移
# l.insert(len(l) >> 1, "middle")
# print(l)
#
# """ 删 """
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # 删除指定元素
# l.remove(1)
# print(l)
# # 删除不存在元素会报错
# # l.remove("not_exist")
#
# # pop是根据索引弹出并获取元素,指定索引必须在范围之内，超出范围会报错
# print(l.pop(0))
# print(l)
# # pop不指定序号，默认删除最后一个元素
# print(l.pop())
# print(l)
# del l[0]
# print(l)
# del l
# # print(l)
#
#
# """ 改 """
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l[0] = '1'
# print(l)
#
# """ 查 """
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# if 8 in l:
#     print(l.index(8))
# # 不存在会报错
# print(l.index("not_exist"))

""" 排序 """
# sort
# l = [1, 5, 3, 7, 2, 9, 4, 8]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# key可以使用lamda表达式 可以是多条件
# l = [1, 5, 3, 7, 2, 9, 4, 8]
# l.sort(key=lambda x: (x % 3, x))
# print(l)
# # key也可以直接调用函数，函数返回值也可以是(1,2,3...)
# l.sort(key=abs)
# print(l)

""" 列表推导式 """
# [表达式 for i in l]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [print(i * 2, end=" ") for i in l]
# print()
# # [表达式 for i in l if 条件式]
# [print(i, end=" ") for i in l if i % 2 == 0]
# print()
# 列表嵌套 一个列表里面又有列表
l = [1, 2, [3, 4, 5, 6], 7, 8, 9, 10]
print(l[2])
# 取出内列表中的元素
print(l[2][0])
