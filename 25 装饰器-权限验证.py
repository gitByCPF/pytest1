# 权限验证装饰器
user_role = "viewer"  # 假设当前用户是 viewer
def permission_required(role):
    """带参数的装饰器：检查用户角色"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role != role:
                print(f"❌ 访问拒绝！{user_role} 无权限执行 {func.__name__}")
                return None
            return func(*args, **kwargs)

        return wrapper

    return decorator

@permission_required("admin")  # 只有 admin 角色才能执行
def delete_post():
    print("🗑️ 删除帖子成功！")
# 带参数的装饰器，语法糖等价于下面的写法，带参数的外部函数是一个普通函数而已
# delete_post = permission_required("admin")(delete_post)
delete_post()