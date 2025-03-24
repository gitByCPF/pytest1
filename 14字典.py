"""
字典：键值对的
字典名 = {key1:value1, key2:value2, key3:value3...}
键具备唯一性，值可以重复
"""
d = {'name': 'jack', 'age': 18, 'address': '湖南'}
print(d)
# 查看元素
print(d.get('name'))  # 键不存在，返回None
print(d.get('exist?', '不存在'))  # 可以设置不存在时候的返回值
print(d['age'])  # 键不存在，报错
# 修改元素
d['age'] = 23
print(d['age'])
# 如果不存在该元素，这就是新增操作
d['gender'] = 'male'
print(d)
# 删除整个字典
# del d
# del d['gender']     # 没有指定的键就会报错
print(d)
# 清空字典内元素，但是保留字典
# d.clear()
print(d)
print(d.pop('gender'))  # 弹出并获取值，键不存在就报错
print(d)
print(d.popitem())  # 出栈弹出最顶层元素（3.7之前是随机删除元素，3.7(含)之后采用有序存储，就变成弹出最后一个元素）
print(d)
# 求长度
print(len(d))
print(d.keys())
print(d.values())
for i in d:
    print("{}: {}".format(i, d[i]))
print(d.items())
# 字典的这些方法返回的都是视图，不是独立存在的数据结构，视图会随着字典的变化而变化
# 想要获得真实存在的数据，可以重新存储
keys_view = d.keys()
keys_real = list(d.keys())
# 字典的应用场景:存储描述物体信息


