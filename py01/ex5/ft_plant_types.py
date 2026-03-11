#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self):
        print(
            f"{self.name} ({self.__class__.__name__}): {self.height}cm"
            f", {self.age} days, {self.color} color\n"
            f"{self.name} is blooming beautifully!\n"
        )


class Tree(Plant):
    def __init__(self, name, height, age, diameter) -> None:
        super().__init__(name, height, age)
        self.diameter: int = diameter

    def produce_shade(self):
        shade = self.height * self.diameter / 100
        print(
            f"{self.name} ({self.__class__.__name__}): {self.height}cm"
            f", {self.age} days, {self.diameter} diameter\n"
            f"{self.name} provides {shade} square meters of shade\n"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, season, nutrient) -> None:
        super().__init__(name, height, age)
        self.season: str = season
        self.nutrient: str = nutrient

    def print_veg(self):
        print(
            f"{self.name} ({self.__class__.__name__}): {self.height}cm"
            f", {self.age} days, {self.season} harvest\n"
            f"{self.name} is rich in {self.nutrient}"
        )


rose = Flower("Rose", 25, 30, "red")
sunflower = Flower("Sunflower", 80, 45, "yellow")
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 400, 1649, 40)
carrot = Vegetable("Carrot", 60, 36, "spring", "vitamin A")
tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

if __name__ == "__main__":
    rose.bloom()
    pine.produce_shade()
    tomato.print_veg()
