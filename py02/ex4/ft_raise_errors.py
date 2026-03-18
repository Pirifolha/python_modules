#!/usr/bin/env python3


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if not plant_name:
            raise ValueError("plant name cannot be empty!")
        else:
            print(f"Plant '{plant_name}' is healthy")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        if int(water_level) > 0 and int(water_level) < 11:
            print("Water levels are fine!")
        else:
            raise ValueError()
    except ValueError:
        if int(water_level) < 1:
            print(f"Error: Water level {water_level} is too low (min 1)")
        else:
            print(f"Error: Water level {water_level} is too high (max 10)")
    try:
        if int(sunlight_hours) > 1 and int(sunlight_hours) < 13:
            print("Sunlight are fine!")
        else:
            raise ValueError()
    except ValueError:
        if int(sunlight_hours) < 2:
            print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        else:
            print(f"Error: Sunlight hours {sunlight_hours} is too high"
                  "(max 12)")


def test_plant_checks():
    print("Testing with good values...")
    check_plant_health("Tomato", 10, 6)
    print("\nTesting error plant name...")
    check_plant_health("", 10, 8)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 0, 8)
    print("\nTesting bad sunglight hours...")
    check_plant_health("tomato", 6, 15)


if __name__ == "__main__":
    test_plant_checks()
