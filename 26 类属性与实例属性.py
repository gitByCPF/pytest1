class Washer:
    name = '滚筒洗衣机'
    brand = '格力'

washer = Washer()

# 类属性，是公共的，类和实例都能访问到
print(washer.name)
print(Washer.name)
print(washer.brand)
print(Washer.brand)

# 实例属性，后添加的，只属于该实例
washer.price = 1450
print(washer.price)
# 类无法访问到实例属性
# print(Washer.price)
washer2 = Washer()
# 其他实例也无法访问
# print(washer2.price)
# 如果想要所有的实例

