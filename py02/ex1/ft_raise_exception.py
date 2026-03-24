#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return 0
    if temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
    elif temp < 0:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!\n")
    return 0


def test_temperature_input() -> None:
    good: str = "25"
    print(f"Testing temperature: {good}")
    if check_temperature(good) != 0:
        print("Crash")
        return

    bad: str = "abc"
    print(f"Testing temperature: {bad}")
    if check_temperature(bad) != 0:
        print("Crash")
        return

    extreme_pos: str = "100"
    print(f"Testing temperature: {extreme_pos}")
    if check_temperature(extreme_pos) != 0:
        print("Crash")
        return

    extreme_neg: str = "-50"
    print(f"Testing temperature: {extreme_neg}")
    if check_temperature(extreme_neg) != 0:
        print("Crash")
        return

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
