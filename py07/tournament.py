#!/usr/bin/env python3

import ex0.classes as c
import ex1.capabilities as cap
import ex2.strategy as strat


def battle(players: list) -> None:
    print("*** Tournament ***")
    print(f"{len(players)} opponents involved")

    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            factory1, strategy1 = players[i]
            factory2, strategy2 = players[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("\n* Battle *")
            print(creature1.describe())
            print("vs")
            print(creature2.describe())
            print("now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except strat.InvalidStrategy as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = c.FlameFactory()
    aqua_factory = c.AquaFactory()
    healing_factory = cap.HealingCreatureFactory()
    transform_factory = cap.TransformCreatureFactory()
    normal_strategy = strat.NormalStrategy()
    aggressive_strategy = strat.AggressiveStrategy()
    defensive_strategy = strat.DefensiveStrategy()

    first_tournament: list[tuple] = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ]
    second_tournament: list[tuple] = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ]
    third_tournamnet: list[tuple] = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]

    print("Tournament 0 (basic)\n[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(first_tournament)
    print("\nTournament 1 (error)\n[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(second_tournament)
    print("\nTournament 2 (multiple)\n[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(third_tournamnet)