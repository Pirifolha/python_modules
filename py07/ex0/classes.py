#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, creature_type: str):
        self.name = name
        self.creature_type = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self):
        pass


class Flameling(Creature):

    def __init__(self, name="Flameling", creature_type="Fire"):
        super().__init__(name, creature_type)

    def attack(self):
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):

    def __init__(self, name="Pyrodon", creature_type="Fire/Flying"):
        super().__init__(name, creature_type)

    def attack(self):
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):

    def __init__(self, name="Aquabub", creature_type="Water"):
        super().__init__(name, creature_type)

    def attack(self):
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):

    def __init__(self, name="Torragon", creature_type="Water"):
        super().__init__(name, creature_type)

    def attack(self):
        return f"{self.name} uses Hydro Pump!"


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):

    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class AquaFactory(CreatureFactory):

    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()
