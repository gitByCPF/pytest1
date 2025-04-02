# 包用于将多个相关的模块组织到一个文件夹中，
# 通过一个特殊的__init__.py文件来初始化包和定义对外接口，
# 从而提高代码结构的清晰性和可维护性，并避免命名冲突
import pkg1
# for name in pkg1.__all__:
#     print(name)
print(pkg1.foo())
# 找不到不对外公开的方法
# print(pkg1.secret())
# 但是可以显性导入来访问，下划线固定内部实现细节只是一种约定，并不是语法规定
from pkg1._internal import secret
print(secret())
