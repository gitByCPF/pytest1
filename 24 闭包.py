# 闭包（Closure）的特征：
# 1.函数嵌套
# 2.内层函数使用外层函数的变量
# 3.外层函数的返回值是内层函数的函数名

# 闭包的本质
# 1.记住状态
# 2.数据封装（类似私有变量）
# 3.函数工厂，动态创建不同功能的函数·

# 实例：计数器
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


increment1 = counter()
print(increment1())
print(increment1())
print(increment1())


# 权限检查
def permission_checker(role):
    """外函数：基于用户角色创建权限检查器"""
    permissions = {
        "admin": ["delete", "edit", "view"],  # 管理员权限最大
        "editor": ["edit", "view"],  # 编辑者只能编辑和查看
        "viewer": ["view"]  # 只能查看
    }

    def check_permission(action):
        """内函数：检查是否允许执行某个操作"""
        nonlocal permissions
        if action in permissions.get(role, []):
            return f"✅ 允许 {role} 执行 {action} 操作"
        else:
            return f"❌ 拒绝 {role} 执行 {action} 操作"

    return check_permission  # 返回一个权限检查函数


# 创建不同角色的权限检查器
admin_checker = permission_checker("admin")
editor_checker = permission_checker("editor")
viewer_checker = permission_checker("viewer")

# 进行权限验证
print(admin_checker("delete"))  # ✅ 允许 admin 执行 delete 操作
print(editor_checker("delete"))  # ❌ 拒绝 editor 执行 delete 操作
print(viewer_checker("view"))  # ✅ 允许 viewer 执行 view 操作
print(viewer_checker("edit"))  # ❌ 拒绝 viewer 执行 edit 操作
