# lambda函数的使用场景
# 1.在 sorted()、max()、min() 中作为 key 参数
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# 按年龄排序
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# 2. 在 map() 中用于批量转换
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# 3. 在 filter() 中用于筛选
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]





