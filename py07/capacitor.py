#!/usr/bin/env python3

import ex0.classes as c
from ex1.capabilities import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: c.CreatureFactory) -> None:

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability\n base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: c.CreatureFactory) -> None:

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability\n base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing(healing_factory)
    print("")
    test_transform(transform_factory)
