#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.height: int = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points: int):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers "
            f"(blooming), Prize points: {self.points}"
        )


class GardenManager:

    total_gardens = 0

    class GardenStats:

        def calculate_points(self, plants: list[Plant]) -> int:
            points = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    points += p.height * p.points
            return points

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def generate_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                print(p)
            elif isinstance(p, FloweringPlant):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"{p.name}: {p.height}cm")

        print(f"\nPlants added: {len(self.plants)}")
        score = self.stats.calculate_points(self.plants)
        print(f"Garden score for {self.owner}: {score}")

    @staticmethod
    def validate_height(value: int) -> bool:
        return value >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list["GardenManager"]:
        return [cls(name) for name in owners]


def main() -> None:

    print("=== Garden Management System Demo ===\n")
    network = GardenManager.create_garden_network(["Alice", "Bob"])
    alice_garden = network[0]
    bob_garden = network[1]

    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print("")

    alice_garden.grow_all()
    print("")
    alice_garden.generate_report()

    print("")
    bob_garden.add_plant(Plant("Bush", 90))
    bob_garden.grow_all()
    bob_score = bob_garden.stats.calculate_points(bob_garden.plants)
    alice_score = alice_garden.stats.calculate_points(alice_garden.plants)

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print(f"Garden scores Alice: " f"{alice_score}, " f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
