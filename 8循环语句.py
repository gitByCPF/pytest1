""" 循环语句 """
# while中的变量必须提前定义
i = 1
while i in range(1, 5):
    print(i)
    i += 1

# # 只要不是false都会判断为真
# while "hhhh" and 1:
#     print("hhhh")

# for循环内的变量不需要提前定义
# 可迭代对象(iterable)：range 字符串 数组
for x in range(5, 10):
    print(x)
# range仅表示次数循环
for x in range(5, 10):
    print("hello")
# 等效于
for x in range(5):
    print("hello")
# range(start, end, stap)
for x in range(1, 10, 2):
    print(x)
for c in "hello":
    print(c)
for i in [1, 2, 3, 4, 5]:
    print(i)
