"""装饰器"""
# 本质：装饰器是一个高阶函数，接收一个函数作为参数，并返回一个新的函数。
# 不修改原函数代码，就能给它动态添加功能。
# 通常使用 @decorator_name 语法，让代码更简洁。
# 支持多个装饰器，可以层层嵌套。
# 支持带参数的装饰器，增强灵活性。
"""装饰器的作用"""
# 日志记录（如函数调用时打印日志）
# 权限控制（检查用户是否有权限执行某些操作）
# 执行时间统计（测量函数运行时间）
# 缓存（避免重复计算，提高效率）
# 输入输出校验（比如参数类型检查）
"""多个装饰器
@decorator1
@decorator2
@decorator3
def my_func():
    pass

等价于：
my_func = decorator1(decorator2(decorator3(my_func)))
执行顺序由外及内，功能应用由内及外
"""

"""装饰器实例"""
# 日志记录装饰器
def log_decorator(func):
    """装饰器：记录函数的调用"""
    def wrapper(*args, **kwargs):
        print(f"📌 正在调用函数 {func.__name__}，参数：{args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ 函数 {func.__name__} 执行完毕，返回值：{result}")
        return result

    return wrapper

# 装饰器语法糖，下面的注解等价于add = log_decorator(add)
@log_decorator
def add(x, y):
    return x + y

add(3, 5)
