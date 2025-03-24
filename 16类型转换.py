# 1.int()转换为整数，可以转换float、纯数字string，开头可以含有+-符号
i = int(1.2)
print(i)
print(type(i))
i = int('-13')  # 1.3就不可以
j = int('+13')
print(i, j)
print(type(i), type(j))

# 2.float()转换为浮点型，特性与int()类似

# 3.str() 任何类型都能转化为字符串
print(str([1, 2, 3]))
print(str({1, 2, 3}))
print(str(1.20))  # 会去除末尾的0

# list()将可迭代对象，转换成列表，支持str tuple dict set
print(list("hello"))
print(list((1, 2, 3)))
# 字典只把键转化为列表
print(list({'name': 'jack', 'age': 20}))
print(list({1, 2, 3, 2, 1, 3}))  # 集合转化为列表，会先去重，再检测

