import time
def timing_decorator(func):
    """计算函数运行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏳ 函数 {func.__name__} 运行耗时：{end - start:.6f} 秒")
        return result
    return wrapper
