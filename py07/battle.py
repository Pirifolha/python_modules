#!/usr/bin/env python3

from ex0.classes import CreatureFactory, FlameFactory, AquaFactory


def test_factories(factory: CreatureFactory) -> None:

    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight(fire: CreatureFactory, aqua: CreatureFactory) -> None:
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
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_factories(flame_factory)
    print("")
    test_factories(aqua_factory)
    print("")
    fight(flame_factory, aqua_factory)
