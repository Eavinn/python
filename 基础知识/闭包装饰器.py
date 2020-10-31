"""
装饰器的本质：
1. 无参数的函数 @dec >> func() == dec(func)()
2. 装饰器带参数 @dec(a) >> func() == dec(a)(func)()
3. 被装饰的函数带参数 @dec >> func(a) == dec(func)(a)
4. 多重装饰器的执行方式如下示例
"""


# def counter(start):
#     def incr():
#         nonlocal start
#         start += 1
#         return start
#     return incr
#
# c1 = counter(5)
# print(c1())
# print(c1())

import time
from time import ctime, sleep


def deco1(deco2_fun):
    print("step2-------------------")

    def deco1_fun(c, d):
        print("step3-------------------")
        deco2_fun(c, d)
        print("step7-------------------")
    return deco1_fun


def deco2(a, b=None):
    print("step1-------------------")

    def temp_fun(my_name):
        print("step1.5--------------")

        def deco2_fun(c, d):
            print("step4-------------------")
            my_name(c, d)
            print(a, b)
            print("step6-------------------")
        return deco2_fun
    return temp_fun


@deco1
@deco2(1, b=2)
# 执行my_name = deco2(1, b=2)(my_name) = temp_fun(my_name) = deco2_fun
# 再执行my_name = deco1(my_name), 装饰前my_name和deco2_fun已经指向一致, 故装饰等同于my_name = deco1(deco2_fun) = deco1_fun(deco2_fun)
# 执行deco1_fun函数体，参数为deco2_fun，于是在函数体内执行函数deco2_fun
# 执行deco2_fun参数体，参数是初始的my_name，于是执行my_name
def my_name(c, d=None):
    print("step5-------------------")


if __name__ == '__main__':
    # 参数（3,4）在my_name被deco2装饰后传给deco2_fun，deco2_fun在被deco1装饰后又将参数传递给deco1_fun
    # deco1_fun接收参数后即可使用，但是在调用deco2_fun函数时仍需要将参数传给子函数，deco2_fun在调用my_name时同理，否则子函数无法顺利执行
    my_name(3, 4)
