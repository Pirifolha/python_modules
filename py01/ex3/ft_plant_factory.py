#!/usr/bin/env python3


class Plant:
    count: int = 0

    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        Plant.count += 1

    def get_info(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 25, 30)
    lilly = Plant("Lilly", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    tulip = Plant("Tulip", 8, 28)
    daisy = Plant("Daisy", 13, 37)
    orchid = Plant("Orchid", 12, 73)
    rose.get_info()
    lilly.get_info()
    cactus.get_info()
    tulip.get_info()
    daisy.get_info()
    orchid.get_info()
    print(f"Total plants created {Plant.count}")


if __name__ == "__main__":
    main()
