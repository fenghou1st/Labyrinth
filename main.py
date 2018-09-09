# -*- coding: utf-8 -*-

"""
迷宫养成游戏（原型）
"""

import argparse

from common import *

FLAGS = None


def main(argv):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_dir',
        type=str,
        default='data',
    )
    parser.add_argument(
        '--dataset_name',
        type=str,
        required=True,
    )

    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)
