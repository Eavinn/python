"""基本运算符号"""
# ** // %

"""字符串常见操作"""
mystr1 = 'hello world itcast and itcastcpp'
mystr2 = 'hello world itcast \n and itcastcpp'
# find, index, count, replace, split, capitalize, title, startswith, endswith, lower, upper, ljust, rjust, center,
# lstrip, rstrip, strip, strip, rfind, rindex, partition, rpartition, splitlines, isalpha, isdigit, isalnum, isspace, join,
print(mystr1.rjust(100))
print(mystr2.splitlines())

"""列表的相关操作"""
# append, extend, insert, index, count, del, pop, sort
a = ['a', 'b', 'c', 'a', 'b']
print(a.index('a', 2, 5))
print(a.count('b'))
a.remove('b')
a.sort(reverse=True)
print(a)

"""元组的相关操作"""
# count, index

"""字典的相关操作"""
# del, clear, len,
info = {'name':'monitor', 'sex':'f', 'address':'China'}
print('清空前,%s'%info)
info.clear()
print('清空后,%s'%info)

a = 100
