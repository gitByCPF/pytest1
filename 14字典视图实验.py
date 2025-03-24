import gc

d = {'name': 'jack', 'age': 18, 'address': '湖南'}
keys_view = d.keys()
# 我们可以根据视图来迭代输出
for key in keys_view:
    print(key)

del d

# 删除字典后，视图仍然可以迭代
for key in keys_view:
    print(key)



