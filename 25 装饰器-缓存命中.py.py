import functools
import decorator

def cache_decorator(func):
    """简单的缓存装饰器"""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"🔄 缓存命中：{args} -> {cache[args]}")
            return cache[args]
        result = func(*args)
        # cache的键是元组，值是int
        cache[args] = result
        print(f"✅ 计算并存入缓存：{args} -> {result}")
        return result

    return wrapper

@decorator.timing_decorator
@cache_decorator
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(30))
