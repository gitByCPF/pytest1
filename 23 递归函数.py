# 递归函数
# 1.存在终止条件
# 2.问题可分解

# 累加1-100的和
def total(n):
    # 终止条件
    if n == 0:
        return 0
    # 问题分解
    return n + total(n - 1)
print(total(100))

# 斐波那契数列 1 1 2 3 5 8...
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
# 时间复杂度O(2^n)非常慢
print(fibonacci(40))
