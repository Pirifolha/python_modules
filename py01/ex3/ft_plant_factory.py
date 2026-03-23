#!/usr/bin/env python3


class Plant:
    count: int = 0

    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth: int) -> None:
        self.height += growth


def main():
    plants = {
        "rose": Plant("Rose", 25, 30),
        "lilly": Plant("Lilly", 80, 45),
        "cactus": Plant("Cactus", 15, 120),
        "tulip": Plant("Tulip", 8, 28),
        "daisy": Plant("Daisy", 13, 37),
        "orchid": Plant("Orchid", 12, 73),
    }

    print(f"Total plants created: {len(plants)}")


if __name__ == "__main__":
    main()
