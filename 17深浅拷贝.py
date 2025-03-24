import copy

# 赋值
# 对象赋值，传递的是引用
# li1 = [1, 2, 3]
# li2 = li1
# li2.append(4)
# print(li1)

# 浅拷贝（shallow copy）：复制对象本身，但嵌套的可变对象仍然共享引用
# 深拷贝（deep copy）：递归复制对象及其所有嵌套元素，保证互不影响
l = [1, 2, 3, [4, 5, 6], 7]
l_shallow = copy.copy(l)
l_deep = copy.deepcopy(l)
# shallow copy
print(id(l) == id(l_shallow))  # False 说明外层不是一个对象
print(id(l[3]) == id(l_shallow[3]))  # True 说明内存够仍然是一个对象
# deep copy
print(id(l) == id(l_deep))  # False 外层不是一个对象
print(id(l[3]) == id(l_deep[3]))  # False 内层也不是一个对象
