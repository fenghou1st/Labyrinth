# -*- coding: utf-8 -*-

"""
各种通用方法
"""

import sys
import os
import pickle
import numpy as np
import pandas as pd

np.set_printoptions(linewidth=200)
pd.options.display.width = 200


def load_cached_data(file_path, message=None):
    """ 从文件系统载入缓存数据 """
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            if not message:
                print('Loaded cached data: {}'.format(os.path.basename(file_path)))
            else:
                print(message)
            return data


def cache_data(data, file_path):
    """ 把数据缓存到文件系统 """
    cache_dir = os.path.dirname(file_path)
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    with open(file_path, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    print('Cached data: {}'.format(os.path.basename(file_path)))


def create_data_frame_from_dict_rows(rows):
    """
    从以行为单位的 dict 列表中构造 DataFrame
    每行为一个 dict，其中 key 是列名，value 是列的值
    每行必须包含同样的 keys

    :param rows:            [{key1: value1, key2: value2, }, ]
    :return:                pandas.DataFrame
    """
    keys = list(rows[0].keys())
    data = {key: [] for key in keys}

    for row in rows:
        for key in keys:
            assert key in row
            data[key].append(row[key])

    return pd.DataFrame(data=data)


def data_frame_to_markdown(data_frame, column_formats):
    """
    获取 DataFrame 的 markdown 格式表示

    :param data_frame:      pandas.DataFrame
    :param column_formats:  column_name -> (width, is_numerical, decimal_width, multiply)
            width:          int - 列数据宽度
            is_numerical:   bool - 是否数字
            decimal_width:  int|None - （若为数字的话）小数点后宽度，为整数时填 0
            multiply:       float|None - （若为数字的话）输出时将乘以该数，为 None 时则忽略此操作
    :return:                str - Markdown 格式的字符串
    """
    column_names = list(data_frame)
    column_widths = {name: column_formats[name][0] for name in column_names}

    column_formats_str = {}
    for name, (width, is_numerical, decimal_width, _) in column_formats.items():
        if is_numerical:
            format_str = '{:<' + str(width) + '.' + str(decimal_width) + 'f}'
        else:
            format_str = '{:' + str(width) + '}'
        column_formats_str[name] = format_str

    text = ''

    # header
    for i, name in enumerate(column_names):
        column_width = column_widths[name]
        if i != 0:
            text += ' | '
        text += ('{:' + str(column_width) + '}').format(name)
    text += '\n'

    # separator
    for i, name in enumerate(column_names):
        column_width = column_widths[name]
        if i != 0:
            text += '-|-'
        text += '-' * column_width
    text += '\n'

    # body
    for _, row in data_frame.iterrows():
        for i, name in enumerate(column_names):
            column_format_str = column_formats_str[name]
            value = row.iat[i]
            _, is_numerical, _, multiply = column_formats[name]
            if is_numerical and multiply is not None:
                value *= multiply
            if i != 0:
                text += ' | '
            text += column_format_str.format(value)
        text += '\n'

    return text
