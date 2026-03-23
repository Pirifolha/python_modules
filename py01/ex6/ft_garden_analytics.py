#!/usr/bin/env python3


class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self, name):
            print(f"[statistics for {name}]")
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._stats = self._Stats()

    def grow(self, cm):
        self.height += cm
        self._stats.grow_calls += 1

    def age_plant(self, days):
        self.age += days
        self._stats.age_calls += 1

    def show(self):
        self._stats.show_calls += 1
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def show_stats(self):
        self._stats.display(self.name)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds=0):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self):
        self.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long "
            f"and {self.trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_stats(self):
        super().show_stats()
        print(f"{self.shade_calls} shade")


def display_plant_stats(plant: Plant):
    plant.show_stats()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose.show_stats()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show_stats()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_plant(20)
    sunflower.bloom()
    sunflower.seeds = 42
    sunflower.show()
    sunflower.show_stats()

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    unknown.show_stats()


if __name__ == "__main__":
    main()
