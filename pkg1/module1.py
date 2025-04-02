def foo():
    """返回 module1 中的foo字符串"""
    return "foo from module1"

class Bar:
    """module1中的Bar类"""
    def __init__(self):
        self.value = "Bar instance from module1"

    def get_value(self):
        return self.value
