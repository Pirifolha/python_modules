#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0 import classes as c


class HealCapability(ABC):

    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):

    def __init__(self, transformed: bool):
        self.transformed = transformed

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(c.Creature, HealCapability):

    def __init__(self, name="Sproutling", creature_type="Grass"):
        super().__init__(name, creature_type)

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self):
        return f"{self.name} heals itself for a small amount"


class Bloomelle(c.Creature, HealCapability):

    def __init__(self, name="Bloomelle", creature_type="Grass/Fairy"):
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self):
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(c.CreatureFactory):

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class Shiftling(c.Creature, TransformCapability):

    def __init__(self, name="Shiftling", creature_type="Normal"):
        c.Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self, transformed=False)

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} shifts into a sharper form"

    def revert(self):
        self.transformed = False
        return f"{self.name} returns to normal"


class Morphgon(c.Creature, TransformCapability):

    def __init__(self, name="Morphgon", creature_type="Normal/Dragon"):
        c.Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self, transformed=False)

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devasting morph strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} morphs into a dragonic form"

    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form"


class TransformCreatureFactory(c.CreatureFactory):

    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphgon()
