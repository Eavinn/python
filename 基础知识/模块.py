"""
1. 当你导入一个模块，Python解析器对模块位置的搜索顺序是：
当前目录
如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

2. 如果一个文件中有__all__变量，那么也就意味着这个变量中的元素，不会被from xxx import *时导入

3. 导包原理：
import 模块 生效条件：init文件加入from . import 文件
from 模块 import * 生效条件：在init文件中的__all__填写相应文件 或 init文件加入from . import 文件
from 模块 import 文件 生效条件：无需任何条件
"""

# import sys
# from 类 import Hero
#
#
# Hero("dd")
# print(Animal('aa'))
#
# print(__name__)
# print(sys.path)


# from importlib import reload
# reload()支持模块重新导入


