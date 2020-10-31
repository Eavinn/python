
"""
abs() 函数返回数字的绝对值。
"""

print(abs(-3434.5))
print(abs(2 + 1j))


"""
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 
function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数算，最后得到一个结果。
"""
from functools import reduce
reduce_list = reduce(lambda a, b: '{}**{}&'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(reduce_list)

"""
random模块
"""
import random
# uniform() 方法将随机生成下一个实数，它在 [x, y] 范围内。
aa = [1, 2, 3, 4]
print(random.uniform(10, 15))
print(random.randint(1, 5))
print(random.random())
print(random.choice(["meng", "liang", "haha"]))

random.shuffle(aa)
print(aa)

# import numpy as np
# print(np.log([1, 3]))

"""
import urllib.parse
# Python3 url编码
print(urllib.parse.quote("天安门"))
# Python3 url解码
print(urllib.parse.unquote("%E5%A4%A9%E5%AE%89%E9%97%A8"))
"""

import urllib.parse

print(urllib.parse.unquote("keyword=%D0%D4%B8%D0%D3%C8%CE%EF&button=%CB%D1%CB%F7", encoding='gbk'))


b = eval("['a', 'b']")
c = eval('1+2')
print(b)
print(c)






