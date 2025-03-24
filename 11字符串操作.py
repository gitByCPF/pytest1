# """ 字符串运算符 """
# # 字符串拼接
# print("hello" + " " + "world")
# print('10' + "10")
# # 重复输出
# print("重复十次\t" * 10)
# # 成员运算符：字符串中是否包含某个子字符串，返回True False
# print("hello" in "hello world")
# print("hello" not in "hello world")
# # 字符串索引（下标从0开始，能快速找到对应的字符）
# print("hello"[0])
# # 超出范围会报错
# # print("hello"[9])
# # 从右往左开始数，下标从-1开始-2 -3 -4....
# print("hello"[-1])

""" 
切片
序列[start:stop:step]
step步长默认是1，表示从左往右截取，每次只走一步来获取字符，此时，左边是头
step是负数，表示从右往左截取，此时，右边是头
[:stop]表示从头开始
[start:]表示直达尾部
[:]表示从头到尾
[start:stop:-1]表示从右往左截取，每次之走一步获取字符
"""
# print("hello"[:-4:-1])
# print("hello"[::-1])
# print("hello"[::])

""" 字符串常见操作 """
# find(self, sub, start, stop) 返回切片第一个字符的索引，范围内不存在该切片则返回-1
# print("hello".find('ll'))
# print("hello".find('not exist'))
# print("hello".find('ll', 2, 4))

# index(self, sub, start, stop)与前面唯一的区别就是，找不到会报错
# print("hello".index('not exist', 2, 4))

# count(self, str, start, stop)统计str在指定范围内出现的次数
# print("hello".count('l', 2, 4))
# print("hello".count('not exist', 2, 4))

# 字符串有很多常用的功能函数
# print("hello".startswith("h"))
# print("hello".startswith("h", 2, 3))
# print("hello".endswith("o"))
# print("hello".upper())
# print("hello".istitle())

# replace(self, old, new, count) 替换切片
print("hello".replace("l", "L"))
print("hello".replace("l", "L", 1))
# 如果指定替换不存在的切片，则无事发生
print("hello".replace("lll", "L"))
print("hello".capitalize()) # 首字母大写

# split()
# 相邻分割元素，会导致结果中出现""空字符
print("hello".split("l"))                   # ['he', '', 'o']
# 末尾作为分隔符，结果也会出现""空字符
print("hello".split("o"))                   # ['hell', '']
# 最多分割次数，默认-1表示无限制
print("hello".split("l", 1))    # ['he', 'lo']
