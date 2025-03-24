""" input输入函数 """
# name = input("请输入名字")
# print(name)

""" 转义字符 """
# 制表符 通常表示空四个字符
print("na\tme")
# 换行符
print("name\n", end="\n")
print("name")
# 回车 表示将当前位置移动到本行开头,如果后接内容，将会覆盖（先删除之前全部内容，再写入）
print("jack\r")
# 转义符号
print("\\,\\t,\\n")
# 原生字符串，默认取消转义
print(r"\ \t \n \\")
