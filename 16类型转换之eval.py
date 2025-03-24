# eval() 函数将字符串当作有效的 Python 表达式来执行，并返回表达式的结果
# 显然，eval容易被注入，不建议使用
result = eval('1+2')
print(result)
print(type(result))

# 不合法的表达式会报错
# eval("1+(1,2,3)")

# 注意！是表达式，不是语句,语句无法执行
# eval("y = 1 + 1") # 这种就是不行的
x = eval("1 + 2")
y = eval("x * 2")
print(x, y)

# 想要执行语句，可以使用exec()
m = 0
n = 0
code1 = "m = 1 + 2"
code2 = "n = m * 2"
exec(code1)
exec(code2)
print(m, n)
