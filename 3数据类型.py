# 数据类型
# 1.整数类型
num = 1
print(type(num))
# 2.浮点型
num = 1.2
print(type(num))
# 3.布尔型
# 布尔值可以当作整形来对待 True是1 False是0
print(type(True))
print(True + False)
# 4.字符串
s = 'hello world'
print(s)
s = "hello world"
print(s)
s = """hello world"""
"""注意区分注释与三引号的字符串赋值，能匹配上就行"""
print(s)

# 5.complex复数型
# z = a + bj a是实部，b是虚部，j是虚数单位
print(type(2+3j))
print((2+3j) + (4+5j))
