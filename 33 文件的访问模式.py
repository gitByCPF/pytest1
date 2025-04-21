def writelines():
    with open('文件的扩展操作.txt', 'w', encoding='utf-8', newline='') as file:
        for i in range(9):
            file.write(str(i + 1) + '\n')
def clean():
    """只写模式打开文件，不写内容，就是清空文件"""
    with open('文件的扩展操作.txt', 'w'):
        pass


# r+ 读写模式 不清空原文件内容，但却从头开始写，写多少覆盖多少
writelines()
with open('文件的扩展操作.txt', 'r+', encoding='utf-8') as f:
    f.write('r+写入内容')

# w+ 读写模式 会清空原文件内容
writelines()
with open('文件的扩展操作.txt', 'w+', encoding='utf-8') as f:
    f.write('w+写入内容')

# a+ 追加读写模式（从文件尾部开始写）
writelines()
