import os
import shutil

# 创建目录
if not os.path.exists('new_dir'):
    os.mkdir('new_dir')
# 创建多层目录
os.makedirs('parent/child')
# 删除多层目录
try:
    os.removedirs('parent/child')
except OSError as e:
    print(e.strerror)
    shutil.rmtree('parent/child')

# 删除文件
with open('需要删除的文件.txt', 'w') as f:
    pass
os.remove('需要删除的文件.txt')
# 复制文件
with open('复制示例文件.txt', 'w', encoding='utf-8') as file:
    file.write('120')
shutil.copy('复制示例文件.txt', '复制后的文件.txt')
# 移动文件
if not os.path.exists('new_dir'):
    os.mkdir('new_dir')
shutil.move('复制后的文件.txt', 'new_dir/移动后的文件.txt')
# 读取大文件
with open('大文件.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
print('********************************************************************')
# 异常处理
try:
    with open('不存在的文件.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("文件未找到")
except IOError:
    print('读写文件失败')
# 文件指针与tell() seek()
with open('文件的扩展操作.txt', 'w', encoding='utf-8') as f:
    f.write('0123456789')
with open('文件的扩展操作.txt', 'r', encoding='utf-8') as f:
    print(f.tell())
    f.seek(5)
    print(f.tell())
    print(f.read())
# 读取图片
with open('profile.jpg', 'rb') as f:
    data = f.read()
    print(data)
with open('new_pic.jpg', 'wb') as f:
    f.write(data)
