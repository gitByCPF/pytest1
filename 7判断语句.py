# 判断语法 冒号不能少
age = 17
if age < 18:
    print("未成年不能上网")

# 比较运算符
a = 1
b = 2
c = 3
d = 4
print(a == b)
print(a > b)
print(a <= b)
print("*********")

# 逻辑运算符
print(a == 1 and b == 1)
print(a == 1 or b == 1)
print(not a == b)

# 三元表达式
num = a if a > b else b
print("a小于b") if a < b else print("a大于b")

# if-else 二选一
# else后面不添加任何东西
if a > b:
    print("a大于b")
else:
    print("b大于a")

# if-elif 多选一
if a > b:
    print("a>b")
elif a == b:
    print("a==b")
elif a < b:
    print("a<b")

# if嵌套
if a > b:
    if a > c:
        if a > d:
            print("a最大")
        else:
            print("d最大")
    elif c > d:
        print("c最大")
    else:
        print("d最大")
elif b > c:
    if b > d:
        print("b最大")
    else:
        print("d最大")
elif c > d:
    print("c最大")
else:
    print("d最大")
