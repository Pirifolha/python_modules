#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


def water_tester() -> None:
    try:
        water: int = 9
        print("Testing WaterError...")
        if water < 10:
            raise WaterError()
    except WaterError as e:
        print(f"Caught {type(e).__name__}: Not enough water in the tank!\n")
    else:
        print("Water level is fine!")


def plant_tester() -> None:
    try:
        age: int = 15
        print("Testing PlantError...")
        if age > 10:
            raise PlantError()
    except PlantError as e:
        print(f"Caught {type(e).__name__}: The tomato plant is wilting!\n")
    else:
        print("Tomato is doing well!")


def garden_tester() -> None:
    try:
        age = 65
        water = 12
        print("Testing catching all garden errors...")
        if age > 10 and water > 10:
            raise GardenError()
    except GardenError as e:
        print(f"Caught a {type(e).__name__}: The tomato plant is wilting!")
        print(f"Caught a {type(e).__name__}: Not enough water in the tank!\n")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    plant_tester()
    water_tester()
    garden_tester()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
