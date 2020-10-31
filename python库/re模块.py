"""
. 匹配任意字符
[] 匹配[]列举字符
\d \D 匹配数字或非数字
\s \S 匹配空白或非空白
\w \W 匹配数字字母下划线或非数字字母下划线
* 匹配0-多个
+ 匹配1-多个
? 匹配0-1次
{m} 匹配m次
{m, n} 匹配m-n次
| 匹配左右任意一个表达式
(ab) 将括号中的字符作为一个分组
\num 引用分组num匹配到的字符串
(?P<xx>) (?P=xx) 分组起别名xx，引用别名为xx的字符串
match, search,
findall, sub, split

python默认贪婪，若要改为非贪婪需要在量纲如"*","?","+","{m,n}"后面加上？
"""

import re

labels = ["<html><h1>www.itcast.cn<h1><html>", "<html><h1>www.itcast.cn</h2></html>"]

for label in labels:
    ret = re.match(r"(<\w*>)(?P<nice><\w*>).*(?P=nice)\1", label)
    if ret:
        print(ret.group())

print(re.findall(r"\D+", "ab1ca2d"))

res1 = re.sub(r"\d+", "998", "python=997")
print(res1)


def func_add(temp):
    """注意参数格式转换"""
    num1 = int(temp.group())
    num1 += 1
    return str(num1)


res2 = re.sub(r"\d+", func_add, "python=997")
print(res2)
res3 = re.split(r":|\s", "info:xiaoZhang 33 shandong")
print(res3)

