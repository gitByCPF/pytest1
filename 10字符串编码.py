""" 字符串编码 """
# ASCII:一个字节存储：数量有限，仅限于全英文
# Unicode:两个字节：转换速度快，但是空间浪费多
# UTF-8:精准，对不同的字符用不同的长度表示，节省空间，但是转换效率低

""" 字符串编码转换 encode decode """
a = "hello"
print(a, type(a))
a1 = a.encode()
# 以字节为单位进行处理
print(a1, type(a1))
a2 = a1.decode()
print(a2, type(a2))

# 编码名称的大小写不影响识别
a = "我是奥特曼"
print(a.encode("utf-8"))
print(a.encode("UTF-8").decode("utf-8"))
