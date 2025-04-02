# raise抛出异常
# raise Exception("我抛出一个异常")
def func():
    raise Exception("我抛出一个异常")


# 捕获异常后可以继续执行
try:
    func()
except Exception as e:
    print(e)
print("捕获异常后可以继续执行")
