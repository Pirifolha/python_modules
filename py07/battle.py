#!/usr/bin/env python3

import ex0.classes as c


def test_factories(factory: c.CreatureFactory) -> None:

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight(fire: c.CreatureFactory, aqua: c.CreatureFactory) -> None:
    f_base = fire.create_base()
    a_base = aqua.create_base()

    print("Testing battle")
    print(f_base.describe())
    print(" vs.")
    print(a_base.describe())
    print(" fight!")
    print(f_base.attack())
    print(a_base.attack())


if __name__ == "__main__":
    flame_factory = c.FlameFactory()
    aqua_factory = c.AquaFactory()
    test_factories(flame_factory)
    print("")
    test_factories(aqua_factory)
    print("")
    fight(flame_factory, aqua_factory)
