class Washer:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    # 不想定义时赋值，必须赋值None
    price = None
    name = "滚筒洗衣机"
    brand = "小米"
    height = 80
    width = 50
    _lifetime = "5年"
    __profit = 10022

    # 实例方法
    def wash(self):
        print("我要洗衣服")

print(Washer.name)
print(Washer.price)
# protected可以在本文件中访问到，但是不会被建议
print(Washer._lifetime)
# print(Washer.profit)

# 实例化
washer = Washer("三空间滚筒洗衣机", "格力")
print(washer.name)

washer.wash()
Washer.wash(washer)
