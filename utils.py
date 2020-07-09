'''
封装常用的工具类
'''
import json


def pathfile(filepath,key):

    # 空列表
    data_list = []

    # 获取数据
    with open(filepath,'r',encoding='utf-8') as file:
        # 转成json数据
        json_data = json.load(file)
        json_values = json_data.get(key)
        # 循环获取字典的值
        data_list.append(list(json_values.values()))

    return data_list