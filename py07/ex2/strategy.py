#!/usr/bin/env python3

from abc import ABC, abstractmethod
import ex0.classes as c
import ex1.capabilities as cap


class BattleStrategy(ABC):

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(c.CreatureFactory, BattleStrategy):
    
    def __init__(self):
        c.Creature.__init__(self, )


class AgressiveStrategy(BattleStrategy):
    pass


class DefensiveStrategy(BattleStrategy):
    pass
