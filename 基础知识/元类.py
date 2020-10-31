# 手工调用type创建类 type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
# MyClass = type('MyClass', (), {'data': 2})
# instance = MyClass()
# print(MyClass, instance)

# python中一切都是对象，类也是对象
# class ObjectCreator(object):
#     def func(self):
#         pass
#
#
# ObjectCreator.new_attribute = 'foo'
# print(hasattr(ObjectCreator, 'func'))
# print(hasattr(ObjectCreator, 'new_attribute'))
# print(ObjectCreator.func)

# type是创建所有类的元类
# print(type(ObjectCreator.func.__class__))
# print(type(ObjectCreator))
# print(type(int))

# 创建自己的元类
# def upper_attr(future_class_name, future_class_parents, future_class_attr):
#     # 当我们定义类时会逐层查找自身及父类的metaclass属性并执行
#
#     # print(future_class_name, future_class_parents, future_class_attr)
#     attrs = ((key, value) for key, value in future_class_attr.items() if not key.startswith('__'))
#     uppercase_attr = dict((key.upper(), value) for key, value in attrs)
#     print(uppercase_attr)
#     return type(future_class_name, future_class_parents, uppercase_attr)
#
#
# class UpperAttrMetaclass(type):
#     def __new__(cls, name, bases, dct):
#         attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
#         uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
#         return super().__new__(cls, name, bases, uppercase_attr)
#
#
# class Foo(object, metaclass=UpperAttrMetaclass):
#     bar = 'bip'
#
#
# print(Foo().BAR)


# 一、首先定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.colmun_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


# 二、定义元类，控制Model对象的创建
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print(name + '-------------------')
        print(attrs)
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            # 保持类属性和列的映射关系到mappings字典
            if isinstance(v, Field):
                print('Found mapping:%s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():  # 将类属性移除，是定义的类字段不污染User类属性，只在实例中可以访问这些key
            attrs.pop(k)
        attrs['__table__'] = name.lower()  # 假设表名为类名的小写，创建类时添加一个__table__属性
        attrs['__mappings__'] = mappings  # 保持属性和列的关系映射，创建类时添加一个__mappings__属性
        print(attrs)
        return super().__new__(cls, name, bases, attrs)


# 三、Model基类
class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))


# 我们想创建类似Django的ORM，只要定义字段就可以实现对数据库表和字段的操作
# 最后、我们使用定义好的ORM接口，使用起来非常简单
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# user = User(id=1, name='Job', email='job@test.com', password='pw')
# user.save()
