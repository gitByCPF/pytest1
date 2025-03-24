s = {1, 2, 3, 4, 5}
s.add(1.0)
print(s)
# 原因是1 1.0的hash值是一样的
print(hash(1))
print(hash(1.0))
print(1 == 1.0)     # True
