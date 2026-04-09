#!/usr/bin/env python3

import random


class Player:
    def __init__(self, name, achievement):
        self.name = name
        self.achievement = achievement

    def create_set(self, len, achievements):
        tmp_list = self.achievement
        i = 0
        while i < len:
            temp = random.randrange(0, len)
            tmp_list.append(achievements[temp])
            i += 1
        self.achievement = set(tmp_list)

    def show(self):
        print(f"Player {self.name}: {self.achievement}")

    def show_common(self, *others):
        print("\nCommon achievements: "
              f"{self.achievement.intersection(*others)}\n")

    def show_unique(self, *others):
        print(f"Only {self.name} has:"
              f" {self.achievement.difference(*others)}\n")

    def show_missing(self, achievements):
        print(
            f"{self.name} is missing: "
            f"{set(achievements).difference(self.achievement)}"
        )


def gen_player_achievements() -> None:
    achievements: list = [
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
    players = [Player(name, []) for name in names]
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
