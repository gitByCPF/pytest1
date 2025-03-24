""" break continue """
for i in range(1, 10):
    print(i)
    if i == 5:
        break
print("************")
x = 1
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1
print("************")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 注意+1操作一定要在continue之前，否则会死循环
x = 1
while x < 10:
    print(x)
    if x == 5:
        continue
    x += 1

