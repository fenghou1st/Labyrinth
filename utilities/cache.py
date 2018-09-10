# -*- coding: utf-8 -*-

import os
import pickle


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
