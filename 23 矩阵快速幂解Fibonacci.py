def matrix_multiply(A, B):
    """计算两个2x2矩阵 A 和 B 的乘积"""
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def matrix_power(matrix, n):
    """计算矩阵的 n 次幂"""
    result = [[1, 0], [0, 1]]  # 单位矩阵
    base = matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        n //= 2
    return result

def fibonacci(n):
    """使用矩阵快速幂计算斐波那契数列的第 n 项"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_power(F, n - 1)
    return result[0][0]

# 示例：计算第100个斐波那契数
print(fibonacci(10000))
