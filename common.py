# -*- coding: utf-8 -*-

"""
Common constants, classes & functions.
"""

import numpy as np
import pandas as pd

np.set_printoptions(linewidth=200)
pd.options.display.width = 200


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
