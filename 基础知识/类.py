__all__ = ["Hero"]
"""
2. 多继承：多继承可以继承多个父类，也继承了所有父类的属性和方法
注意：如果多个父类中有同名的 属性和方法，则默认使用第一个父类的属性和方法（根据类的魔法属性mro的顺序来查找）
3. super()调用父类方法，便于父类名修改后遗症
4. 私有权限：在属性名和方法名 前面 加上两个下划线 __， 类的私有属性 和 私有方法，都不能通过对象直接访问，但是可以在本类内部访问；都不会被子类继承，子类也无法访问；
    _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
5. 类属性和类方法：类属性只能被实例对象访问，不能被实例对象修改和删除.

classname.__doc__: 获取类描述信息
classname.__dict__: 类属性和方法
classname.__mro__: 类继承链条
obj.__module__: 当前操作的对象在哪那个模块
obj.__class__: 当前操作的对象的类
obj.__dict__: 实例属性
obj.__call__: obj()调用
"""


class Hero(object):
    """类的描述信息，__doc__方法调用"""
    address = '山东'
    __switch = True

    def __new__(cls, *args, **kwargs):
        print("__new__方法被调用")
        return object.__new__(cls)

    def __init__(self, name):
        print('__init__方法被调用')
        self.name = name
        self.kind = "aa"
        self.address = '上海'

    def __str__(self):
        return "打印对象时，调用__str__方法"

    def __del__(self):
        print("__del__方法被调用")

    def __call__(self, *args, **kwargs):
        print("__call__方法被调用")


spider = Hero("spider")
spider()
