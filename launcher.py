# -*- coding: utf-8 -*-

"""
Launcher of the game.
"""

import sys
import argparse

from game import Game

FLAGS = None


def main(argv):
    game = Game(FLAGS)
    game.run()


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
