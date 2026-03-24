#!/usr/bin/env python3


class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise InvalidPlant
            else:
                print(f"Watering {plant}")
    except InvalidPlant as e:
        print(f"Error: Cannot water {plant} - {type(e).__name__}!")
    finally:
        print("Closing watering system (cleanup)\n")


def test_watering_system() -> None:
    plant_list: list = ["tomato", "lettuce", "carrots"]
    inv_plant_list: list = [None, "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(inv_plant_list)


if __name__ == "__main__":
    test_watering_system()
