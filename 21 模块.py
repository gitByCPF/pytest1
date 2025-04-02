# 一个py文件就是一个模块，即导入一个模块本质上就是执行一个py文件
# 1.内置模块：random time os logging functools等
# 2.第三方模块（第三方库）
# 下载模块：pip install 模块名
# 卸载模块：pip uninstall 模块名
# 查看下载的模块列表 pip list
# 3.自定义模块：命名要遵循标识符固定及变量的命名规范，并且不要与内置或者导入的第三方模块命名冲突

# 导入模块
# 方式一：import 模块名1，模块名2...（通常一个个导入）
# 方式二：from 模块名 import 功能1,功能2... (不建议使用，因为很多功能命名会有冲突)
# from module import * = import module

# 给模块起别名：import module as alias
# 给功能起别名：from module import funa as a, funb, func as c

# __name__ 是一个内置变量，它表示当前模块的名称。
# 其作用主要体现在区分模块是被 直接运行 还是 被导入
# 如果 Python 文件被直接运行，__name__ 的值为 "__main__"。
print(__name__)
# 如果 Python 文件被作为模块导入，__name__ 的值是该模块的文件名（不带后缀)
import module1
print(module1.__name__)
# 如果你希望模块可以作为独立脚本运行，又能被导入时避免执行某些代码，可以这样写：
if __name__ == '__main__':
    print("独立脚本执行时输出")



