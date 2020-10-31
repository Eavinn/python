"""
linux终端 默认字符串编码是utf-8，windows终端 默认字符串编码是gbk。
默认python2 解释器编码是ascii，所以不能处理包含中文的unicode字符串。所以在python2中直接保存u“你好”会报错
"""



import json
import csv


def json_to_csv():
    json_data = json.load(open('temp/aqi.json', 'r'))
    csv_writer = csv.writer(open('temp/aqi.csv', 'w'))
    table_title = json_data[0].keys()
    table_list = [data.values() for data in json_data]
    print(table_title)
    print(table_list)

    csv_writer.writerow(table_title)
    csv_writer.writerows(table_list)

    csv_writer.close()

json_to_csv()