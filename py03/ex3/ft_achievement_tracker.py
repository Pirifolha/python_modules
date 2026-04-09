#!/usr/bin/env python3

import random
from typing import List, Set


class Player:
    def __init__(self, name: str, achievement: Set[str]) -> None:
        self.name = name
        self.achievement = achievement

    def create_set(self, length: int, achievements: List[str]) -> None:
        temp: List[str] = random.sample(achievements, length)
        for t in temp:
            self.achievement.add(t)

    def show(self) -> None:
        print(f"Player {self.name}: {self.achievement}")

    def show_common(self, *others: Set[str]) -> None:
        print("\nCommon achievements: "
              f"{self.achievement.intersection(*others)}\n")

    def show_unique(self, *others: Set[str]) -> None:
        print(f"Only {self.name} has:"
              f" {self.achievement.difference(*others)}\n")

    def show_missing(self, achievements: List[str]) -> None:
        print(
            f"{self.name} is missing: "
            f"{set(achievements).difference(self.achievement)}"
        )


def gen_player_achievements() -> None:
    achievements: List[str] = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]

    names = ["Bob", "Alice", "Charlie", "Dylan"]
    players = [Player(name, set()) for name in names]
    for player in players:
        player.create_set(random.randint(1, 13), achievements)
        player.show()

    print(f"\nAll distinct achievements: {set(achievements)}")

    other_achievements = [player.achievement for player in players[1:]]
    players[0].show_common(*other_achievements)

    for player in players:
        others = [p.achievement for p in players if p != player]
        player.show_unique(*others)

    for player in players:
        player.show_missing(achievements)


if __name__ == "__main__":
    gen_player_achievements()
