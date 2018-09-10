# -*- coding: utf-8 -*-

from enum import Enum, auto
from abc import ABC
from typing import Union

from common import *


class CharacterClass(Enum):
    FIGHTER = auto()
    ROGUE = auto()
    WIZARD = auto()
    CLERIC = auto()


class Direction(Enum):
    N = Point(0, 1)
    NE = Point(1, 1)
    E = Point(1, 0)
    ES = Point(1, -1)
    S = Point(0, -1)
    SW = Point(-1, -1)
    W = Point(-1, 0)
    NW = Point(-1, 1)


class Character(ABC):
    def __init__(self) -> None:
        self.name = str()
        self.char_class = CharacterClass()
        self.exp = int()
        self.level = int()
        self.attack = float()
        self.defence = float()
        self.magic_attack = float()
        self.magic_defence = float()
        self.hp = float()
        self.mp = float()
        self.stamina = float()

    def move(self, direction: Direction) -> None:
        pass

    def interact(self, target: Facility) -> None:
        pass

    def attack(self, attack_type: AttackType, target: 'Character') -> None:
        pass

    def heal(self, target: 'Character') -> None:
        pass

    def on_attacked(self, attack_type: AttackType, attack_point: float) -> None:
        pass

    def on_healed(self, heal_point: float) -> None:
        pass
