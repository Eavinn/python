"""单例模式, 只有一个实例，只初始化一次"""


class Singleton(object):
    """单例模式"""
    __instance = None
    __is_first = True

    # 注意new和init方法的传参
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if self.__is_first:
            self.age = age
            self.name = name
            Singleton.__is_first = False


a = Singleton(18, "dongGe")
print(a.age)
b = Singleton(8, "dongGe")
print(a.age)

print(id(a))
print(id(b))
a.age = 19
print(b.age)
