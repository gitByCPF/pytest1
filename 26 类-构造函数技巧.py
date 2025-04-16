"""
构造方法只能是一个__init_()
默认参数可以模拟多个构造器的行为，但是只能按从左到右顺序来判定
"""
class Washer:
    def __init__(self, name=None, brand=None):
        self.name = name if name else "滚筒洗衣机"
        self.brand = brand if brand else "小米"

    name = None
    brand = None


w1 = Washer()
print(w1.name)
w2 = Washer("新的滚筒机")
print(w2.name)
w3 = Washer(None, "格力")
print(w3.brand)


"""类方法可以构建丰富的实例化方式"""
class AirConditioner:
    def __init__(self, name=None, brand=None):
        self.name = name if name else "变频空调"
        self.brand = brand if brand else "格力"

    name = None
    brand = None

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["brand"])

    @classmethod
    def from_str(cls, data):
        name, brand = data.split(',')
        return cls(name, brand)

ac1 = AirConditioner()
print(ac1.__dict__)
ac2 = AirConditioner("中央空调", "小米")
print(ac2.__dict__)
ac3 = AirConditioner.from_dict({'name': '玫瑰空调', 'brand': '董氏'})
print(ac3.__dict__)
ac4 = AirConditioner.from_str('立式空调,美的')
print(ac4.__dict__)
