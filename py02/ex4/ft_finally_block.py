#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


def water_plants(plant_name: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_name:
            if plant == plant.capitalize():
                print(f"Watering {plant}: [OK]")
            else:
                raise PlantError()
    except PlantError as e:
        print(f"Caught {type(e).__name__}: Invalid plant name to water: "
              f"'{plant}'\n...ending tests and returning to main")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    plant_list: list = ["Tomato", "Lettuce", "Carrots"]
    inv_plant_list: list = ["Tomato", "Lettuce", "carrots"]
    print("Testing valid plants...")
    water_plants(plant_list)
    print("Testing invalid plants...")
    water_plants(inv_plant_list)


if __name__ == "__main__":
    test_watering_system()
