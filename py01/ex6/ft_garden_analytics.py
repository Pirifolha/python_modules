#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} grew {self.cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points: int):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return print(
            f"{self.name}: {self.height}cm, {self.color} flowers"
            f"(blooming), Prize points: {self.points}"
        )


class GardenManager:

    total_gardens = 0


# class GardenStats:
