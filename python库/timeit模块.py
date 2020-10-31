"""
测试代码执行效率，
"""
from timeit import Timer


def t1():
    l = []
    for i in range(1000):
        l = l + [i]


def t2():
    l = []
    for i in range(1000):
        l.append(i)


def t3():
    l = [i for i in range(1000)]


def t4():
    l = list(range(1000))


timer1 = Timer("t1()", "from __main__ import t1")
print("concat ",timer1.timeit(number=1000), "seconds")
timer2 = Timer("t2()", "from __main__ import t2")
print("append ",timer2.timeit(number=1000), "seconds")
timer3 = Timer("t3()", "from __main__ import t3")
print("comprehension ",timer3.timeit(number=1000), "seconds")
timer4 = Timer("t4()", "from __main__ import t4")
print("list range ",timer4.timeit(number=1000), "seconds")
