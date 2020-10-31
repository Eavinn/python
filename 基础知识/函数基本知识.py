import time
from functools import reduce
"""
全局变量：
1. 全局变量能够在所有的函数中进行访问，但是无法重新赋值，赋值操作则被理解为对未定义的局部变量修改；
2. 当函数内出现局部变量和全局变量相同名字时，函数内部中的 变量名 = 数据 此时理解为定义了一个局部变量
2. 若要在函数中对全局变量赋值则需要提前定义变量为global
"""

"""
不定长参数：
1. *args： ∗的作用：函数接受实参时，按顺序分配给函数形参，如果遇到带∗的形参，那么就把还未分配出去的实参以元组形式打包（pack）,分配给那个带∗的形参
2. **kwargs： 把多个关键字参数打包成字典
"""

"""
递归函数的使用场景：随着传参的规律变化值要出现相应地规律性变化
"""

"""
lambda 函数的使用场景
"""
# 1. 将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
add = lambda x, y: x+y
print(add(2, 5))

# 2. 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换.
time.sleep = lambda x: None
time.sleep(5)

# 3. 将lambda函数作为其他函数的返回值，返回给调用者。
# return lambda x, y: x+y

# 4. 将lambda函数作为参数传递给其他函数。
filter_list = [i for i in filter(lambda x: x % 3 == 0, [1, 2, 3])]
print(filter_list)

sorted_list = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
print(sorted_list)

map_list = map(lambda x: x + 2, [1, 2, 3])
print(map_list)

reduce_list = reduce(lambda a, b: '{}**{}&'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(reduce_list)

import Hero
Hero("ss").exc_catch()
