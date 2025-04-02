# 定义函数
from typing import List


def total(a, b):
    return a + b
# 调用函数
print(total(1, 2))

# 返回值
# 1. 一个返回值也没有，返回的是None
# 2. 一个返回值，就把该值返回给调用者
# 3. 多个返回值，以元组的形式返回给调用者
def sort_key(x):
    return x % 2, x

l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.sort(key=sort_key)
print(l)


