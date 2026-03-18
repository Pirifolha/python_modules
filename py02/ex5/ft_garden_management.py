#!/usr/bin/env python3


class InvalidName(Exception):
    pass


class InvalidLevel(Exception):
    pass


class InvalidLight(Exception):
    pass


class Plant:
    def __init__(self, name: str, water: int, sunlight: int):
        self.name = name
        self.water = water
        self.sunlight = sunlight


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name, water, sunlight):
        try:
            if not name:
                raise InvalidName("Plant name cannot be empty!")
            plant = Plant(name, water, sunlight)
            print(f"Added {plant.name} successfully!")
            self.plants.append(plant)
        except InvalidName as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, water):
        print("\nOpening watering system")
        try:
            for plant in self.plants:
                try:
                    plant.water += water
                    if plant.water > 10:
                        raise InvalidLevel(
                            f"Error watering {plant.name}: Water level "
                            f"{plant.water} is too high (max 10)"
                        )
                    print(f"Watering {plant.name} - success")
                except InvalidLevel as e:
                    print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self):
        print("\nChecking plant health")
        for plant in self.plants:
            try:
                if plant.water > 11 or plant.water < 1:
                    raise InvalidLevel(
                        f"Error checking {plant.name}: Water level"
                        f" {plant.water} is invalid"
                    )
                elif plant.sunlight < 2 or plant.sunlight > 12:
                    raise InvalidLight(
                        f"Error checking {plant.name}: Sunlight level"
                        f" {plant.sunlight} is invalid"
                    )
                else:
                    print(
                        f"{plant.name}: healthy (water: {plant.water},"
                        f" sun: {plant.sunlight})"
                    )
            except (InvalidLevel, InvalidLight) as e:
                if plant.water < 1:
                    print(f"{e} Water level {plant.water} is too low (min 1)")
                elif plant.water > 11:
                    print(f"{e} Water level {plant.water} is too high"
                          " (max 10)")
                if plant.sunlight < 2:
                    print(f"{e} Sunlight hours {plant.sunlight} is too low"
                          "(min 2)")
                elif plant.sunlight > 12:
                    print(
                        f"{e} Sunlight hours {plant.sunlight}"
                        " is too high (max 12)"
                    )


def test_garden_management():

    manager = GardenManager()

    manager.add_plant("tomato", 8, 6)
    manager.add_plant("lettuce", 13, 6)
    manager.add_plant("", 8, 6)
    manager.water_plants(1)
    manager.check_health()

    print("\nTesting error recovery...")
    try:
        raise InvalidLevel("Not enough water in tank")
    except InvalidLevel as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...\n")

    manager.add_plant("carrot", 5, 5)
    manager.check_health()


if __name__ == "__main__":
    test_garden_management()
