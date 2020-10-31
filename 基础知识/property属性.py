class Goods1(object):
    def __init__(self):
        self.__original_price = 100
        self.__discount = 0.8

    @property
    def price(self):
        new_price = self.__original_price * self.__discount
        return new_price

    @price.setter
    def price(self, value):
        # 方便重新实现属性的设置和读取方法，可做边界设定
        if type(value) is not int:
            print("error:不是整型数字")
        self.__original_price = value

    @price.deleter
    def price(self):
        del self.__original_price


class Goods2(object):
    def __init__(self):
        self.__original_price = 100
        self.__discount = 0.8

    def get_price(self):
        new_price = self.__original_price * self.__discount
        return new_price

    def set_price(self, value):
        self.__original_price = value

    def del_price(self):
        del self.__original_price

    # 使用类属性定义property属性
    price = property(get_price, set_price, del_price)

obj = Goods1()
# obj = Goods2()
print(obj.price)
obj.price = 20
print(obj.price)
del obj.price
