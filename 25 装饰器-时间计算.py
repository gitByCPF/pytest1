import time
"""
实现了around的切片作用
"""
def timing_decorator(func):
    """计算函数运行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏳ 函数 {func.__name__} 运行耗时：{end - start:.6f} 秒")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)  # 模拟耗时操作
    print("函数执行完毕")

slow_function()
