#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self):
        print(f"{self.name} : {self.height}, {self.age} days old")

    def grow(self, growth: int) -> None:
        self.height += growth

    def age_plant(self, days_to_age: int, growth_per_day: int = 1) -> int:
        height_before = self.height

        self.age += days_to_age
        self.grow(days_to_age * growth_per_day)

        return self.height - height_before


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def show_flower(self):
        print(
            f"=== Flower\n"
            f"{self.name} : {self.height}cm, {self.age} days old\n"
            f"Color: {self.color}\n"
            f"{self.name} has not bloomed yet!"
        )

    def bloom(self):
        print(
            f"[asking the {self.name} to bloom]\n"
            f"{self.name} : {self.height}cm, {self.age} days old\n"
            f"Color: {self.color}\n"
            f"{self.name} is blooming beautifully!\n"
        )


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def show_tree(self):
        print(
            f"=== Tree\n"
            f"{self.name}: {self.height}cm, {self.age} days\n"
            f"Trunk diameter: {self.trunk_diameter}"
        )

    def produce_shade(self):
        print(
            f"[asking the oak to produce shade]\n"
            f"{self.__class__.__name__} {self.name} now provides a shade of "
            f"{self.height}cm long and {self.trunk_diameter} wide\n"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, season, nutritional_value) -> None:
        super().__init__(name, height, age)
        self.season: str = season
        self.nutritional_value: str = nutritional_value

    def show_veg(self):
        print(
            f"{self.name}: {self.height}cm, {self.age} days old\n"
            f"Harvest season: {self.season}\n"
            f"Nutritional value: {self.nutritional_value}"
        )

    def grow_and_age(self, days, growth_per_day=1, nutrition_per_day=1):
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        self.age_plant(days, growth_per_day)
        self.nutritional_value += days * nutrition_per_day


rose = Flower("Rose", 25, 30, "red")
sunflower = Flower("Sunflower", 80, 45, "yellow")
oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 400, 1649, 40)
carrot = Vegetable("Carrot", 60, 36, "spring", "vitamin A")
tomato = Vegetable("Tomato", 5.0, 10, "April", 0)

if __name__ == "__main__":
    rose.show_flower()
    rose.bloom()
    pine.show_tree()
    pine.produce_shade()
    tomato.show_veg()
    tomato.grow_and_age(20, growth_per_day=2, nutrition_per_day=1)
    tomato.show_veg()
