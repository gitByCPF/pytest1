# 不建议在__init————中写业务逻辑
# print("__init__.py中的语句会在导包时就被运行执行")
# if __name__ == "__main__":
#     print("单独执行才会运行的代码")

# 从当前包的子模块中导入希望对外暴露的成员
from .module1 import foo, Bar
from .module2 import baz

# 定义 __all__ 列表，指定当使用 'from my_package import *' 时导入的名称
__all__ = ['foo', 'Bar', 'baz']


