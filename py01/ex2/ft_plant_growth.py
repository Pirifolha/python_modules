#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, cm) -> None:
        self.height += cm

    def age_plant(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    day: int = 1
    growth: int = 1
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.get_info()
        rose.grow(growth)
        rose.age_plant()
        day += 1
    print(f"Growth this week: +{growth*6}cm")


if __name__ == "__main__":
    main()
