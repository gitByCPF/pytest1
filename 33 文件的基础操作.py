import os
# 分类：文本文件、二进制文件
# 只读
f = open('example.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
# 只写
f = open('example.txt', 'w', encoding='utf-8')
f.write('只写的内容')
f.close()
# 追加
f = open('example.txt', 'a', encoding='utf-8')
f.write('\nadded content')
f.close()
# 读写模式(+不能单独使用，可以配合使用r+ w+ a+ x+)
f = open('example.txt', 'r+', encoding='utf-8')
print(f.read())
f.write('\n可读可写内容')
f.close()
# 只许新建不许覆盖
if os.path.exists('new.txt'):
    os.remove('new.txt')
f = open('new.txt', 'x+', encoding='utf-8')
print(f.read())
f.write('只许新建不许覆盖')
f.close()

print("****************************")
# with open会自动关闭文件，更推荐
with open('example.txt', 'r+', encoding='utf-8') as f:
    print(f"第一行内容:{f.readline()}")
    # 读指针会一直移动，下面代码只能从第二行读起
    lines = f.readlines()
    print(lines)
