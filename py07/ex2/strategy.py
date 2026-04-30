#!/usr/bin/env python3

from abc import ABC, abstractmethod
import ex0.classes as c
import ex1.capabilities as cap


class InvalidStrategy(Exception):
    def __init__(self, creature, strategy_name: str = "strategy"):
        creature_name = creature.__class__.__name__
        super().__init__(f"Invalid Creature '{creature_name}' for this {strategy_name} strategy")


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature):
        return True

    def act(self, creature):
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        if hasattr(creature, "transform"):
            return True
        else:
            return False

    def act(self, creature):
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidStrategy(creature, "aggressive")


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature):
        if hasattr(creature, "heal"):
            return True
        else:
            return False

    def act(self, creature):
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidStrategy(creature, "defensive")
