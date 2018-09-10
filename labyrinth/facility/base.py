# -*- coding: utf-8 -*-

"""
Facility of the labyrinth (base class).
"""

from abc import ABC
import numpy as np
from character import Character


class Facility(ABC):
    def __init__(self) -> None:
        """
        shape:              shape: (width, height), type: int8
                            A 2d-array, in which non-zero value outlines the shape of this object.
                            The position of this object is (width // 2, height // 2).
        passable:           type: bool
                            Whether this object can be passed.
        """
        self.shape = np.ones((1, 1), dtype=np.int8)
        self.passable = bool()

    def on_pass(self, character: Character) -> None:
        pass

    def on_interactive(self, character: Character) -> None:
        pass
