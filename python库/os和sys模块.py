import sys
import os

# 通过sys.argv获取程序外部传入

"""os基本操作方法"""
# rename, remove, mkdir, getcwd, chdir, listdir, rmdir
print(os.getcwd())
os.chdir("../")
print(os.getcwd())
print(os.listdir())
